#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    vector<int> isVisited(max(N, K + K / 2 + 1));
    deque<pair<int, int>> q;
    isVisited[N] = true;
    q.push_back({N, 0});

    while (!q.empty())
    {
        pair<int, int> c = q.front();
        int p = c.first;
        int t = c.second;
        q.pop_front();

        if (p == K)
        {
            cout << t;
            return 0;
        }

        for (int next : {p - 1, p + 1, p * 2})
        {
            if (0 <= next && next <= max(N, K + K / 2 + 1) && !isVisited[next])

            {
                isVisited[next] = true;
                (next == p * 2) ? q.push_front({next, t}) : q.push_back({next, t + 1});
            }
        }
    }

    return 0;
}
