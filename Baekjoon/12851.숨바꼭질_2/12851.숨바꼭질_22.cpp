#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    vector<int> time(66'667 * 2, 1e7);
    vector<int> count(66'667 * 2, 0);

    time[N] = 0;
    ++count[N];
    queue<int> q;
    q.push(N);

    while (!q.empty())
    {
        int current = q.front();
        q.pop();

        for (int next : {current - 1, current + 1, current * 2})
            if (0 <= next && next < 66'667 * 2)
            {
                if (time[next] > time[current] + 1)
                {
                    time[next] = time[current] + 1;
                    count[next] = count[current];
                    q.push(next);
                }

                else if (time[next] == time[current] + 1)
                    count[next] += count[current];
            }
    }

    cout << time[K] << '\n'
         << count[K];

    return 0;
}
