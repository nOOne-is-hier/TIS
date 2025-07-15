#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N, M;
int s, e;

void dijkstra(vector<vector<pair<int, int>>> &adjacencyList, vector<int> &dist, priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> &pq)
{
    dist[s] = 0;
    pq.push({0, s});

    while (!pq.empty())
    {
        pair<int, int> cu = pq.top();
        pq.pop();

        if (cu.second == e)
        {
            cout << cu.first;
            return;
        }

        if (cu.first > dist[cu.second])
            continue;

        for (pair<int, int> vw : adjacencyList[cu.second])
            if (dist[vw.first] > dist[cu.second] + vw.second)
            {
                dist[vw.first] = dist[cu.second] + vw.second;
                pq.push({dist[vw.first], vw.first});
            }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;

    vector<vector<pair<int, int>>> adjacencyList(N + 1);
    vector<int> dist(N + 1, 1e9);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    int u, v, w;
    for (int i = 1; i <= M; ++i)
    {
        cin >> u >> v >> w;
        adjacencyList[u].emplace_back(v, w);
    }

    cin >> s >> e;

    dijkstra(adjacencyList, dist, pq);

    return 0;
}
