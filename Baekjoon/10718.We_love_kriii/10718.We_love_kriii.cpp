// 10718 – We love kriii
// https://www.acmicpc.net/problem/10718
// solved.ac: https://solved.ac/search?query=10718
// 시간 제한: 1 초
// 메모리 제한: 256 MB
// 티어: 🟫 Bronze V
// 태그: 구현
// 푼 사람 수: 185,231
// 평균 시도: 1.52

#include <iostream>
#if defined(_WIN32)
#include <io.h>
#include <cstdio>
#else
#include <unistd.h>
#include <cstdio>
#endif

using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  // 표준입력이 터미널이면 input.txt로 대체 (파이프 입력 시에는 그대로 cin)
#if defined(_WIN32)
  if (_isatty(_fileno(stdin)))
  {
    freopen("input.txt", "r", stdin);
  }
#else
  if (isatty(fileno(stdin)))
  {
    freopen("input.txt", "r", stdin);
  }
#endif

  cout << "강한친구 대한육군\n강한친구 대한육군";
  return 0;
}
