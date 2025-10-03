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
#include <vector>
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

  vector<int> dp(n + 1, 1e6);
  dp[0] = 0;
  if (n >= 2)
    dp[2] = 1;
  if (n >= 5)
    dp[5] = 1;

  for (int i = 1; i <= n; ++i)
  {
    if (i - 2 >= 0)
      dp[i] = min(dp[i], dp[i - 2] + 1);
    if (i - 5 >= 0)
      dp[i] = min(dp[i], dp[i - 5] + 1);
  }

  cout << (dp[n] < 1e6 ? dp[n] : -1);
  return 0;
}
