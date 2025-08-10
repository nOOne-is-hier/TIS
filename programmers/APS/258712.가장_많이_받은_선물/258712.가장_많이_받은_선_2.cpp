#include <algorithm>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;

int solution(vector<string> friends, vector<string> gifts)
{
    int n = (int)friends.size();
    unordered_map<string, int> id;
    id.reserve(n);
    for (int i = 0; i < n; ++i)
        id[friends[i]] = i;

    vector<vector<int>> cnt(n, vector<int>(n, 0));
    vector<int> given(n, 0), received(n, 0);

    for (const string &g : gifts)
    {
        size_t sp = g.find(' ');
        int a = id[g.substr(0, sp)];  // from
        int b = id[g.substr(sp + 1)]; // to
        ++cnt[a][b];
        ++given[a];
        ++received[b];
    }

    vector<int> gift_index(n);
    for (int i = 0; i < n; ++i)
        gift_index[i] = given[i] - received[i];

    vector<int> next_received(n, 0);
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (i == j)
                continue;
            int a = cnt[i][j]; // i→j
            int b = cnt[j][i]; // j→i
            if (a != b)
            {
                if (a > b)
                    next_received[i]++;
            }
            else
            {
                if (gift_index[i] > gift_index[j])
                    next_received[i]++;
            }
        }
    }

    return *max_element(next_received.begin(), next_received.end());
}
