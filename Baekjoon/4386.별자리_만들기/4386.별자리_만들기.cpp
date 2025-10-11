#include <cmath>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;
  vector<pair<double, double>> stars(n);
  for (auto &star : stars)
    cin >> star.first >> star.second;

  vector<vector<double>> adjacency_matrix(n, vector<double>(n, 0));
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j)
      adjacency_matrix[i][j] = hypot(stars[i].first - stars[j].first, stars[i].second - stars[j].second);

  vector<bool> visited(n, false);
  priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> pq;
  pq.emplace(0, 0);
  double result = 0;
  int cnt = 0;
  while (!pq.empty() && cnt < n)
  {
    auto [w, u] = pq.top();
    pq.pop();
    if (visited[u])
      continue;
    visited[u] = true;
    result += w;
    ++cnt;

    for (int i = 0; i < n; ++i)
      if (!visited[i])
        pq.emplace(adjacency_matrix[u][i], i);
  }

  cout << result;

  return 0;
}
