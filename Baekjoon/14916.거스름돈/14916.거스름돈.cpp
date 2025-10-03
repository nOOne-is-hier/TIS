// 14916 – 거스름돈
// https://www.acmicpc.net/problem/14916
// solved.ac: https://solved.ac/search?query=14916
// 시간 제한: 2 초
// 메모리 제한: 512 MB
// 티어: ⚪ Silver V
// 태그: 그리디 알고리즘, 다이나믹 프로그래밍, 수학
// 푼 사람 수: 13,812
// 평균 시도: 2.14

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

  int n;
  cin >> n;

  int coins = -1;
  for (int i = 4; i >= 0; --i)
  {
    int rest, temp = 0;
    temp += i;
    if (n - i * 2 >= 0)
    {
      rest = n - i * 2;

      if (rest % 5 == 0)
        coins = temp + rest / 5;
    }
  }

  cout << coins;
  return 0;
}
