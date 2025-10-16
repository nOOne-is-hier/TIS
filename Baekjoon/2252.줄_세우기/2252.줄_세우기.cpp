// 2252 – 줄 세우기
// https://www.acmicpc.net/problem/2252
// solved.ac: https://solved.ac/search?query=2252
// 시간 제한: 2 초
// 메모리 제한: 128 MB
// 티어: 🟡 Gold III
// 태그: 그래프 이론, 방향 비순환 그래프, 위상 정렬
// 푼 사람 수: 26,893
// 평균 시도: 1.71

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

  int N, M;
  cin >> N >> M;

  vector<vector<int>> adjacency_list(N + 1);
  vector<int> in_degrees(N + 1, 0);
  while (M--)
  {
    int A, B;
    cin >> A >> B;
    adjacency_list[A].push_back(B);
    ++in_degrees[B];
  }

  queue<int> q;
  for (int student = 1; student <= N; ++student)
    if (in_degrees[student] == 0)
      q.push(student);

  while (!q.empty())
  {
    int cur = q.front();
    q.pop();

    cout << cur << ' ';

    for (int &nxt : adjacency_list[cur])
      if (--in_degrees[nxt] == 0)
        q.push(nxt);
  }

  return 0;
}
