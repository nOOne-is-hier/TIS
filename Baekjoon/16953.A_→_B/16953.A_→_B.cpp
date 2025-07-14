#include <iostream>
#include <queue>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int A, B;
    cin >> A >> B;

    int count{};

    while (A < B)
    {
        if (B % 10 == 1)
        {
            B /= 10;
            ++count;
        }
        else if (B % 2 == 0)
        {
            B /= 2;
            ++count;
        }
        else
            break;
    }

    cout << (A == B ? count + 1 : -1);

    // queue<pair<long long, int>> q;
    // q.push({A, 0});

    // while (q.size() > 0)
    // {
    //     pair<long long, int> c = q.front();
    //     q.pop();
    //     long long current = c.first;
    //     int count = c.second;

    //     if (current == B)
    //     {
    //         cout << count + 1;
    //         return 0;
    //     }

    //     if (current * 2 <= B)
    //         q.push({current * 2, count + 1});
    //     if (current * 10 + 1 <= B)
    //         q.push({current * 10 + 1, count + 1});
    // }

    // cout << -1;
    return 0;
}
