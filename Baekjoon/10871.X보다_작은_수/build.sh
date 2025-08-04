#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
echo ":돋보기: 현재 디렉토리의 C++ 파일 목록:"
select file in *.cpp; do
  if [[ -n "$file" ]]; then break; fi
done
exe="main.exe"
echo ":톱니바퀴: 컴파일: $file → $exe"
g++ "$file" -std=c++14 -O2 -o "$exe"
echo ":흰색_확인_표시: 빌드 완료, 실행:"
if [[ -f input.txt ]]; then
  ./"$exe" < input.txt
else
  ./"$exe"
fi
