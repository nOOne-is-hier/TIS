#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, E;
int u, v;
vector<vector<pair<int, int>>> adjacencyList;

int dijkstra(int s, int e)
{
    vector<int> dist(N + 1, 1e8);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    dist[s] = 0;
    pq.push({0, s});

    while (!pq.empty())
    {
        pair<int, int> current = pq.top();
        pq.pop();
        int cc = current.first;
        int cn = current.second;

        if (cn == e)
            return cc;

        for (pair<int, int> &next : adjacencyList[cn])
        {
            int nc = next.second;
            int nn = next.first;

            if (dist[nn] > cc + nc)
            {
                dist[nn] = cc + nc;
                pq.push({cc + nc, nn});
            }
        }
    }

    return dist[e];
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> E;
    adjacencyList.resize(N + 1);

    int a, b, c;
    for (int i = 1; i <= E; ++i)
    {
        cin >> a >> b >> c;
        adjacencyList[a].push_back({b, c});
        adjacencyList[b].push_back({a, c});
    }

    cin >> u >> v;

    int result = min(dijkstra(1, u) + dijkstra(u, v) + dijkstra(v, N), dijkstra(1, v) + dijkstra(v, u) + dijkstra(u, N));
    cout << ((result >= 1e8) ? -1 : result);

    return 0;
}
