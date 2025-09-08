// 5666 – Hot Dogs
// https://www.acmicpc.net/problem/5666
// solved.ac: https://solved.ac/search?query=5666
// 시간 제한: 1 초
// 메모리 제한: 128 MB
// 티어: 🟫 Bronze III
// 태그: 구현, 사칙연산, 수학
// 푼 사람 수: 1,209
// 평균 시도: 1.62

#include <iostream>
#include <iomanip>
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

  float H, P;
  while (cin >> H && cin >> P)
  {
    cout << fixed << setprecision(2) << H / P << '\n';
  }
  return 0;
}
