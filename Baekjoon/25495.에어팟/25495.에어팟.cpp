// 25495 – 에어팟
// https://www.acmicpc.net/problem/25495
// solved.ac: https://solved.ac/search?query=25495
// 시간 제한: 1 초
// 메모리 제한: 1024 MB
// 티어: 🟫 Bronze II
// 태그: 구현, 시뮬레이션
// 푼 사람 수: 771
// 평균 시도: 2.04

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
  int last_used = 0;
  int streak = 0;
  int current_used = 0;
  while (N--)
  {
    int iphone;
    cin >> iphone;

    if (last_used != iphone)
    {
      last_used = iphone;
      current_used += 2;
      streak = 1;
    }

    else if (last_used == iphone)
      current_used += (1 << ++streak);

    if (current_used >= 100)
    {
      current_used = 0;
      last_used = 0;
      streak = 0;
    }
  }

  cout << current_used;

  return 0;
}
