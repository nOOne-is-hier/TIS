// 1516 – 게임 개발
// https://www.acmicpc.net/problem/1516
// solved.ac: https://solved.ac/search?query=1516
// 시간 제한: 2 초
// 메모리 제한: 128 MB
// 티어: 🟡 Gold III
// 태그: 그래프 이론, 다이나믹 프로그래밍, 방향 비순환 그래프, 위상 정렬
// 푼 사람 수: 10,804
// 평균 시도: 2.05

#include <iostream>
#include <queue>
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

  int N;
  cin >> N;
  vector<vector<int>> adjacency_list(N + 1);
  vector<int> times(N + 1, 0), in_degrees(N + 1, 0), dp(N + 1, 0);

  for (int i = 1; i <= N; ++i)
  {
    int time;
    cin >> time;
    times[i] = time;

    while (true)
    {
      int prv;
      cin >> prv;
      if (prv == -1)
        break;
      adjacency_list[prv].push_back(i);
      ++in_degrees[i];
    }
  }

  queue<int> q;
  for (int i = 1; i <= N; ++i)
    if (in_degrees[i] == 0)
    {
      q.push(i);
      dp[i] = times[i];
    }

  while (!q.empty())
  {
    int cur = q.front();
    q.pop();

    for (int &nxt : adjacency_list[cur])
    {
      dp[nxt] = max(dp[nxt], dp[cur] + times[nxt]);
      if (--in_degrees[nxt] == 0)
        q.push(nxt);
    }
  }

  for (int i = 1; i <= N; ++i)
    cout << dp[i] << '\n';

  return 0;
}
