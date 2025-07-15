#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int N, K;
vector<pair<int, int>> items;
vector<vector<int>> memo;

// DFS + 백트래킹
// void recursion(int package, int weight, int loadOutValue, vector<pair<int, int>> &packages, vector<vector<int>> &weights, vector<bool> &isVisited)
// {

//     for (int i = package; i < N; ++i)
//     {
//         if (weight + packages[i].first <= K && !isVisited[i] && weights[package][weight + packages[i].first] < loadOutValue + packages[i].second)
//         {
//             weights[package][weight + packages[i].first] = loadOutValue + packages[i].second;
//             isVisited[i] = true;
//             recursion(i + 1, weight + packages[i].first, loadOutValue + packages[i].second, packages, weights, isVisited);
//             isVisited[i] = false;
//         }
//     }
// }

// int dfs()
// {

//     vector<pair<int, int>> packages(N);
//     for (pair<int, int> &wv : packages)
//         cin >> wv.first >> wv.second;
//     vector<vector<int>> weights(100, vector<int>(K + 1));
//     vector<bool> isVisited(N);

//     recursion(0, 0, 0, packages, weights, isVisited);

//     int loadOutValueMax = 0;
//     for (vector<int> &row : weights)
//         loadOutValueMax = max(loadOutValueMax, *max_element(row.begin(), row.end()));

//     return loadOutValueMax;
// }

// top-down
int dfs(int i, int w)
{
    if (i == N)
        return 0;
    if (memo[i][w] != -1)
        return memo[i][w];
    int pass = dfs(i + 1, w);
    int pick = 0;
    if (w >= items[i].first)
        pick = dfs(i + 1, w - items[i].first) + items[i].second;

    return memo[i][w] = max(pass, pick);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K;

    items.resize(N);
    for (pair<int, int> &item : items)
        cin >> item.first >> item.second;

    memo.resize(N, vector<int>(K + 1, -1));

    cout << dfs(0, K);
    cout << '\n';

    // bottom-up
    // vector<pair<int, int>> packages(N);
    // for (pair<int, int> &package : packages)
    //     cin >> package.first >> package.second;

    // vector<int> dp(K + 1);

    // for (int i = 0; i < N; ++i)
    // {
    //     int w = packages[i].first;
    //     int v = packages[i].second;

    //     for (int j = K; j >= w; --j)
    //         dp[j] = max(dp[j], dp[j - w] + v);
    // }

    // cout << *max_element(dp.begin(), dp.end());
    // cout << dfs();

    return 0;
}
