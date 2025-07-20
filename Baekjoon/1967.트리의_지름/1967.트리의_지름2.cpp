#include <iostream>
#include <vector>

using namespace std;

int N;
vector<vector<pair<int, int>>> adjacencyList;
vector<bool> is_visited;
int farthest_node = 0;
int max_dist = 0;

void dfs(int v, int dist)
{
    is_visited[v] = true;

    if (max_dist < dist)
    {
        max_dist = dist;
        farthest_node = v;
    }

    for (pair<int, int> &next : adjacencyList[v])
    {
        int nv = next.first;
        int nw = next.second;
        if (!is_visited[nv])
            dfs(nv, nw + dist);
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    adjacencyList.resize(N + 1);

    for (int i = 1; i < N; ++i)
    {
        int p, c, w;
        cin >> p >> c >> w;

        adjacencyList[p].emplace_back(c, w);
        adjacencyList[c].emplace_back(p, w);
    }

    is_visited.assign(N + 1, false);
    dfs(1, 0);

    is_visited.assign(N + 1, false);
    max_dist = 0;
    dfs(farthest_node, 0);

    cout << max_dist;

    return 0;
}
