#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

file=$(ls *.cpp | head -n1)
exe=main.exe

echo "⚙️ 컴파일: $file → $exe"
g++ "$file" -std=c++14 -O2 -o "$exe"

echo "✅ 빌드 완료, 파일 생성 확인:"
ls -l "$exe"

echo "▶ 실행 결과 (input.txt 있으면 리다이렉트):"
if [[ -f input.txt ]]; then
  ./"$exe" < input.txt
else
  ./"$exe"
fi
