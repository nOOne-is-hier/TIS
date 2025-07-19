#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int V, E, K;
vector<int> dist;
vector<vector<pair<int, int>>> adjacencyList;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> V >> E >> K;

    dist.resize(V + 1, 1e8);
    adjacencyList.resize(V + 1);

    for (int i = 1; i <= E; ++i)
    {
        int u, v, w;
        cin >> u >> v >> w;

        adjacencyList[u].push_back({w, v});
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    dist[K] = 0;
    pq.push({0, K});

    while (!pq.empty())
    {
        pair<int, int> current = pq.top();
        pq.pop();
        int cc = current.first;
        int cn = current.second;

        for (pair<int, int> &next : adjacencyList[cn])
        {
            int nc = next.first;
            int nn = next.second;

            if (dist[nn] > cc + nc)
            {

                dist[nn] = cc + nc;
                pq.push({cc + nc, nn});
            }
        }
    }

    for (int i = 1; i <= V; ++i)
        if (dist[i] == 1e8)
            cout << "INF" << '\n';
        else
            cout << dist[i] << '\n';

    return 0;
}
