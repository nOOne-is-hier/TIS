#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
shopt -s nullglob

# ─────────────────────────────────────────────────────────────
# 0) 공통 유틸
#   - unixify: CRLF→LF 정규화 + 마지막 줄 개행(LF) 보장
#     (gawk의 RS/RT를 이용해 EOF 개행 유무를 정확히 처리)
#   - normalize_ws: unixify 포함 + 각 행의 '행끝 공백' 제거
#                   + 파일 끝의 연속된 빈 줄 제거 + 마지막 개행 보장
# ─────────────────────────────────────────────────────────────
unixify() {
  gawk 'BEGIN{RS="\r?\n"; ORS=""}
       { printf "%s", $0; if (RT!="") printf "\n" }
       END { if (NR>0 && RT=="") printf "\n" }'
}
normalize_ws() {
  gawk 'BEGIN{RS="\r?\n"; ORS=""; n=0}
       {
         sub(/[ \t]+$/, "", $0);      # 행끝 공백 제거
         n++; a[n]=$0
       }
       END {
         # 파일 끝의 연속된 빈 줄 제거
         while (n>0 && a[n]=="") n--;
         for (i=1; i<=n; i++) printf "%s\n", a[i];
         if (n==0) printf "\n";       # 비어있는 파일도 개행 1개 보장
       }'
}
have() { command -v "$1" >/dev/null 2>&1; }

# ─────────────────────────────────────────────────────────────
# 1) 소스 선택
# ─────────────────────────────────────────────────────────────
pick="${1:-}"
cands=( *.cpp *.py *.java )
if [[ -z "${pick}" ]]; then
  if [[ ${#cands[@]} -eq 0 ]]; then
    echo "소스 파일이 없습니다."; exit 1
  fi
  echo "🔎 실행할 소스 선택:"
  select pick in "${cands[@]}"; do
    [[ -n "${pick:-}" ]] && break
  done
fi
[[ -f "$pick" ]] || { echo "유효한 소스 파일이 아닙니다: $pick"; exit 1; }

# ─────────────────────────────────────────────────────────────
# 2) C++이면 UCRT64로 재실행(bounce)
#    (이미 UCRT64면 그대로 진행)
#    - 임시파일 대신 환경변수로 인자 전달 → /tmp 불일치 이슈 제거
# ─────────────────────────────────────────────────────────────
ext="${pick##*.}"
MSYS_NOW="${MSYSTEM:-}"
if [[ "$ext" == "cpp" && "$MSYS_NOW" != "UCRT64" ]]; then
  UCRT_BASH="/c/msys64/usr/bin/bash.exe"
  UCRT_ENV="/c/msys64/usr/bin/env.exe"

  if [[ -x "$UCRT_BASH" && -x "$UCRT_ENV" ]]; then
    echo "↪ UCRT64로 재실행(bash.exe -lc)"
    # PICK_ARG 환경변수로 안전하게 전달 (경로/공백/한글 대비)
    exec "$UCRT_ENV" MSYSTEM=UCRT64 CHERE_INVOKING=1 PICK_ARG="$pick" \
         "$UCRT_BASH" -lc "cd \"$PWD\"; bash ./run.sh \"\$PICK_ARG\""
  else
    echo "❗ UCRT bash를 찾을 수 없습니다: $UCRT_BASH (또는 env.exe)"
    exit 1
  fi
fi

# ─────────────────────────────────────────────────────────────
# 3) 입력 파일 목록
# ─────────────────────────────────────────────────────────────
inputs=( tests/*.in )
if [[ ${#inputs[@]} -eq 0 ]]; then
  inputs=( input.txt )
fi

mkdir -p out

# ─────────────────────────────────────────────────────────────
# 4) 언어별 빌드/실행 커맨드 준비
# ─────────────────────────────────────────────────────────────
run_cmd() { :; }  # placeholder
case "$ext" in
  cpp)
    gpp="C:/msys64/ucrt64/bin/g++.exe"
    [[ -x "$gpp" ]] || gpp="g++"
    exe="./main.exe"
    echo "⚙️  compile: $pick -> $exe"
    "$gpp" "$pick" -std=c++14 -O2 -pipe -static -s -o "$exe"
    run_cmd() { ./main.exe; }
    ;;
  py)
    run_cmd() { python -X utf8 "$pick"; }
    ;;
  java)
    JAVA_BUILD_DIR="${JAVA_BUILD_DIR:-}"
    if [[ -z "$JAVA_BUILD_DIR" ]]; then
      build_dir="$(mktemp -d)"
      CLEAN_BUILD=1
    else
      build_dir="$JAVA_BUILD_DIR"
      mkdir -p "$build_dir"
      CLEAN_BUILD=0
    fi
    trap '[[ "${CLEAN_BUILD:-0}" == "1" ]] && rm -rf "$build_dir"' EXIT

    echo "⚙️  javac -encoding UTF-8 -d \"$build_dir\" $pick"
    javac -encoding UTF-8 -d "$build_dir" "$pick"
    run_cmd() { java -Dfile.encoding=UTF-8 -cp "$build_dir" Main; }
    ;;
  *)
    echo "알 수 없는 확장자: $pick"; exit 1 ;;
esac

# ─────────────────────────────────────────────────────────────
# 5) 실행 & 검증
#    - normalize_ws 로 행끝 공백/마지막 개행 차이 무시
#    - diff 없으면 cmp fallback
# ─────────────────────────────────────────────────────────────
for in_file in "${inputs[@]}"; do
  tmp_out="$(mktemp)"
  out_file="out/$(basename "$pick").$(basename "$in_file").out"
  echo "▶ $pick < $(basename "$in_file")"
  run_cmd < "$in_file" > "$tmp_out" || true

  exp=""
  if [[ "$in_file" == tests/*.in ]]; then
    exp="${in_file%.in}.out"
  fi

  if [[ -n "$exp" && -f "$exp" ]]; then
    if have diff; then
      if diff -u <(normalize_ws < "$exp") <(normalize_ws < "$tmp_out") > /dev/null; then
        echo "✅ PASS"
      else
        echo "❌ FAIL"
        diff -u <(normalize_ws < "$exp") <(normalize_ws < "$tmp_out") || true
      fi
    else
      exp_n="$(mktemp)"; tmp_n="$(mktemp)"
      normalize_ws < "$exp" > "$exp_n"
      normalize_ws < "$tmp_out" > "$tmp_n"
      if cmp -s "$exp_n" "$tmp_n"; then
        echo "✅ PASS (cmp)"
      else
        echo "❌ FAIL (cmp) — 시스템에 diff가 없어 상세 비교는 생략"
        echo "---- expected (head) ----"; head -n 40 "$exp_n" || true
        echo "---- actual   (head) ----"; head -n 40 "$tmp_n" || true
        echo "-------------------------"
      fi
      rm -f "$exp_n" "$tmp_n"
    fi
  else
    echo "ℹ️  비교용 정답 파일 없음"
  fi

  mv -f "$tmp_out" "$out_file"
done
