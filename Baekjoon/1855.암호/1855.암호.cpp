// 암호 (1855)
// https://www.acmicpc.net/problem/1855

#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int K;

    string s;

    cin >> K >> s;

    int multiplicand = s.length() / K;

    for (int i = 0; i < K; ++i)
        for (int j = 0; j < multiplicand; ++j)
        {
            if (j % 2 == 0)
                cout << s[K * j + i];
            else if (j % 2 == 1)
                cout << s[K * j + K - i - 1];
        }

    return 0;
}
