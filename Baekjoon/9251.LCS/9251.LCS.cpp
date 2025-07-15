#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s1, s2;
    cin >> s1 >> s2;

    int N = s1.length();
    int M = s2.length();

    vector<vector<int>> dp(N, vector<int>(M));

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            dp[i][j] = (s1[i] == s2[j] ? (i > 0 && j > 0 ? dp[i - 1][j - 1] + 1 : 1) : (i > 0 && j > 0 ? max(dp[i - 1][j], dp[i][j - 1]) : (i > 0 ? dp[i - 1][j] : (j > 0 ? dp[i][j - 1] : 0))));

    cout << dp[N - 1][M - 1];

    return 0;
}
