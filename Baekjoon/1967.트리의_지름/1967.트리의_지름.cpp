#include <iostream>
#include <tuple>
#include <vector>

using namespace std;

int N;
vector<vector<pair<int, int>>> adjacencyList;
vector<pair<int, int>> dp;

int dfs(int v, int pw)
{
    if (adjacencyList[v].empty())
        return pw;

    for (pair<int, int> &next : adjacencyList[v])
    {
        int nv = next.first;
        int nw = next.second;
        int w = dfs(nv, nw);
        if (dp[v].first < w)
        {
            dp[v].second = dp[v].first;
            dp[v].first = w;
        }
        else if (dp[v].second < w)
            dp[v].second = w;
    }

    return dp[v].first + pw;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    adjacencyList.resize(N + 1);
    dp.resize(N + 1, {0, 0});

    for (int i = 1; i < N; ++i)
    {
        int p, c, w;
        cin >> p >> c >> w;

        adjacencyList[p].push_back({c, w});
    }

    dfs(1, 0);

    int result = 0;
    for (pair<int, int> &node : dp)
        result = max(result, node.first + node.second);

    cout << result;

    return 0;
}
