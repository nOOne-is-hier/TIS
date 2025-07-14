#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<vector<int>> table(N, vector<int>(N));
    for (vector<int> &line : table)
        for (int &cell : line)
            cin >> cell;

    vector<vector<int>> dp = table;

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            dp[i][j] += (i > 0 ? dp[i - 1][j] : 0) + (j > 0 ? dp[i][j - 1] : 0) - (i > 0 && j > 0 ? dp[i - 1][j - 1] : 0);

    while (M--)
    {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        cout << dp[x2 - 1][y2 - 1] - (y1 > 1 ? dp[x2 - 1][y1 - 2] : 0) - (x1 > 1 ? dp[x1 - 2][y2 - 1] : 0) + (x1 > 1 && y1 > 1 ? dp[x1 - 2][y1 - 2] : 0) << '\n';
    }

    return 0;
}
