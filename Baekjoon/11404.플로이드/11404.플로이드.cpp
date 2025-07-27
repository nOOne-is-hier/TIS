#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    int i, j, k;

    vector<vector<int>> dist(N + 1, vector<int>(N + 1, 1e7));

    while (M)
    {
        cin >> i >> j >> k;
        dist[i][j] = min(dist[i][j], k);
        --M;
    }

    for (k = 1; k <= N; ++k)
        for (i = 1; i <= N; ++i)
            for (j = 1; j <= N; ++j)
                if (i != j)
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);

    for (i = 1; i <= N; ++i, cout << '\n')
        for (j = 1; j <= N; ++j, cout << ' ')
            cout << (dist[i][j] != 1e7 ? dist[i][j] : 0);

    return 0;
}
