// 5522 – 카드 게임
// https://www.acmicpc.net/problem/5522
// solved.ac: https://solved.ac/search?query=5522
// 시간 제한: 1 초
// 메모리 제한: 256 MB
// 티어: 🟫 Bronze V
// 태그: 사칙연산, 수학
// 푼 사람 수: 21,067
// 평균 시도: 1.21

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

  int A, result = 0;
  for (int i = 0; i < 5; ++i)
  {
    cin >> A;
    result += A;
  }

  cout << result;

  return 0;
}
