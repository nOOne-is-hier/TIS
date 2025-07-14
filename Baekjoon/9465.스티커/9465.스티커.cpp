#include <iostream>
#include <vector>

using namespace std;

int T, N;

int dfs(int r, int c, vector<vector<int>> &memo, vector<vector<int>> &stickers)
{
    if (c < 0)
        return 0;
    if (memo[r][c] != -1)
        return memo[r][c];

    return memo[r][c] = max(dfs(1 - r, c - 1, memo, stickers), dfs(1 - r, c - 2, memo, stickers)) + stickers[r][c];
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> T;

    for (int i = 1; i <= T; ++i)
    {

        cin >> N;

        vector<vector<int>> stickers(2, vector<int>(N));
        for (vector<int> &line : stickers)
            for (int &sticker : line)
                cin >> sticker;

        vector<vector<int>> memo(2, vector<int>(N, -1));

        cout << max(dfs(0, N - 1, memo, stickers), dfs(1, N - 1, memo, stickers)) << '\n';

        // vector<vector<int>> dp = stickers;

        // for (int c = 1; c < N; ++c)
        //     for (int r = 0; r < 2; ++r)
        //         for (int d = 1; d <= 2; ++d)
        //             if (0 <= c - d)
        //                 dp[r][c] = max(dp[r][c], dp[(r + 1) % 2][c - d] + stickers[r][c]);

        // cout << max(dp[0][N - 1], dp[1][N - 1]) << '\n';
    }

    return 0;
}
