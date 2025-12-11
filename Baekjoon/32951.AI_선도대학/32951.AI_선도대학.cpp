// 32951 – AI 선도대학
// https://www.acmicpc.net/problem/32951
// solved.ac: https://solved.ac/search?query=32951
// 시간 제한: 1 초
// 메모리 제한: 1024 MB
// 티어: 🟫 Bronze V
// 태그: 사칙연산, 수학
// 푼 사람 수: 3,392
// 평균 시도: 1.13

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

  int N;
  cin >> N;
  cout << N - 2024;
  return 0;
}
