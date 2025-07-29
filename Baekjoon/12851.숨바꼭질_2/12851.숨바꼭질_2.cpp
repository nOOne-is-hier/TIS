#include <iostream>
#include <queue>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    int visited[66'667 * 2];
    fill(begin(visited), end(visited), 1e7);
    queue<pair<int, int>> q;

    visited[N] = 0;
    q.push({0, N});
    int count = 0;
    while (!q.empty())
    {
        pair<int, int> current = q.front();
        q.pop();
        int cc = current.first;
        int cp = current.second;

        if (cp == K)
        {
            ++count;
            continue;
        }

        for (int np : {cp - 1, cp + 1, cp * 2})
            if (0 <= np && np < 66'667 * 2 && visited[np] >= cc + 1 && visited[K] >= visited[np])
            {
                visited[np] = cc + 1;
                q.push({cc + 1, np});
            }
    }

    cout << visited[K] << '\n'
         << count;

    return 0;
}
