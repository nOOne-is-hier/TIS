// 13302 – 리조트
// https://www.acmicpc.net/problem/13302
// solved.ac: https://solved.ac/search?query=13302
// 시간 제한: 2 초
// 메모리 제한: 512 MB
// 티어: 🟡 Gold III
// 태그: 다이나믹 프로그래밍
// 푼 사람 수: 2,151
// 평균 시도: 2.28

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

  int N, M;
  cin >> N >> M;
  vector<int> visit(N + 1, 1);
  while (M--)
  {
    int day;
    cin >> day;
    visit[day] = 0;
  }

  const int COUPONS = 40;
  vector<vector<int>> dp(COUPONS + 1, vector<int>(N + 1, 1e9));

  dp[0][0] = 0;
  for (int j = 1; j <= N; ++j)
  {
    for (int i = 0; i <= COUPONS; ++i)
    {
      if (!visit[j])
        dp[i][j] = dp[i][j - 1];

      dp[i][j] = min(dp[i][j], dp[i][j - 1] + 10'000);

      if (i >= 1 && j >= 3)
        dp[i][j] = min(dp[i][j], dp[i - 1][j - 3] + 25'000);

      if (i >= 2 && j >= 5)
        dp[i][j] = min(dp[i][j], dp[i - 2][j - 5] + 37'000);

      if (i <= COUPONS - 3)
        dp[i][j] = min(dp[i][j], dp[i + 3][j - 1]);
    }
  }

  int result = 1e9;
  for (int i = 0; i <= COUPONS; ++i)
    result = min(result, dp[i][N]);

  cout << result;

  return 0;
}
