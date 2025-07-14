#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<vector<int>> costs(N, vector<int>(3));
    for (vector<int> &line : costs)
        for (int &cost : line)
            cin >> cost;

    vector<vector<int>> dp(N, vector<int>(3, 1e9));

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < 3; ++j)
            for (int k = 0; k < 3; ++k)
            {
                if (i == 0)
                    dp[i][j] = costs[i][j];
                else if (j != k && dp[i][j] > dp[i - 1][k] + costs[i][j])
                    dp[i][j] = dp[i - 1][k] + costs[i][j];
            }

    cout << *min_element(dp.back().begin(), dp.back().end());

    return 0;
}
