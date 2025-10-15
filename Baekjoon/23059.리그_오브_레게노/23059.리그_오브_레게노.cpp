// 23059 – 리그 오브 레게노
// https://www.acmicpc.net/problem/23059
// solved.ac: https://solved.ac/search?query=23059
// 시간 제한: 2 초
// 메모리 제한: 512 MB
// 티어: 🟡 Gold II
// 태그: 그래프 이론, 방향 비순환 그래프, 위상 정렬, 자료 구조, 집합과 맵, 해시를 사용한 집합과 맵
// 푼 사람 수: 444
// 평균 시도: 2.89

#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
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
  vector<vector<int>> adjacency_list(4e5);
  vector<int> in_degrees(4e5, 0);

  vector<string> names;
  names.reserve(4e5);
  unordered_map<string, int> indices;
  indices.reserve(4e5 * 2);

  int idx = 0;
  while (N--)
  {
    string A, B;
    cin >> A >> B;
    if (indices.find(A) == indices.end())
    {
      indices.emplace(A, idx++);
      names.push_back(A);
    }
    if (indices.find(B) == indices.end())
    {
      indices.emplace(B, idx++);
      names.push_back(B);
    }

    adjacency_list[indices[A]].push_back(indices[B]);
    ++in_degrees[indices[B]];
  }

  int cnt = names.size();
  priority_queue<pair<int, string>, vector<pair<int, string>>, greater<pair<int, string>>> pq;
  for (int i = 0; i < cnt; ++i)
    if (!in_degrees[i])
      pq.emplace(0, names[i]);

  vector<string> result;
  result.reserve(cnt);
  while (!pq.empty())
  {
    auto [step, cur] = pq.top();
    pq.pop();
    result.push_back(cur);

    for (int &nxt : adjacency_list[indices[cur]])
      if (--in_degrees[nxt] == 0)
        pq.emplace(step + 1, names[nxt]);
  }

  if (result.size() < cnt)
    cout << -1;

  else
    for (string &item : result)
      cout << item << '\n';

  return 0;
}
