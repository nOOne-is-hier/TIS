// 26209 – Intercepting Information
// https://www.acmicpc.net/problem/26209
// solved.ac: https://solved.ac/search?query=26209
// 시간 제한: 1 초
// 메모리 제한: 1024 MB
// 티어: 🟫 Bronze V
// 태그: 구현
// 푼 사람 수: 3,124
// 평균 시도: 1.31

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

  int bit;
  while (cin >> bit)
  {
    if (bit == 9)
    {
      cout << 'F';
      return 0;
    }
  }
  cout << 'S';
  return 0;
}
