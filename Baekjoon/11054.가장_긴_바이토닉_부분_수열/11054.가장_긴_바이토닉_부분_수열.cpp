#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<vector<int>> dp(3, vector<int>(N + 2));

    int elem;
    for (int i = 1; i <= N; ++i)
    {
        cin >> dp[0][i];

        for (int j = 0; j < i; ++j)
            if (dp[0][j] < dp[0][i])
                dp[1][i] = max(dp[1][i], dp[1][j] + 1);
    }

    for (int i = 1; i <= N; ++i)
    {
        for (int j = 0; j < i; ++j)
            if (dp[0][N + 1 - j] < dp[0][N + 1 - i])
                dp[2][N + 1 - i] = max(dp[2][N + 1 - i], dp[2][N + 1 - j] + 1);
    }

    int result = 0;
    for (int i = 0; i <= N; ++i)
    {
        result = max(result, dp[1][i] + dp[2][i] - 1);
    }

    cout << result;
    return 0;
}
