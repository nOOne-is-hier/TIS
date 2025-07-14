// #include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int dfs(int N, int r, int c, vector<vector<int>> &memo, vector<vector<int>> &triangle)
{
    if (r == N - 1)
        return triangle[r][c];
    if (memo[r][c] != -1)
        return memo[r][c];
    return memo[r][c] = max(dfs(N, r + 1, c, memo, triangle), dfs(N, r + 1, c + 1, memo, triangle)) + triangle[r][c];
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<vector<int>> triangle(N);
    for (int i = 0; i < N; ++i)
    {
        triangle[i].resize(i + 1);
        for (int &number : triangle[i])
            cin >> number;
    }

    vector<vector<int>> memo(N, vector<int>(N, -1));

    cout << dfs(N, 0, 0, memo, triangle);

    // vector<vector<int>> dp = triangle;

    // for (int i = 0; i < N; ++i)
    //     for (int j = 0; j < i + 1; ++j)
    //         for (int k = 0; k < 2; ++k)
    //             dp[i][j] = max(dp[i][j], (i > 0 && 0 <= j - k && j - k < i) ? dp[i - 1][j - k] + triangle[i][j] : 0);

    // cout << *max_element(dp.back().begin(), dp.back().end());
    return 0;
}
