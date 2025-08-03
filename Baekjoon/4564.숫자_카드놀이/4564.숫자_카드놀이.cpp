#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int S;

    while (cin >> S, S != 0)
    {
        while (S != S % 10)
        {
            cout << S << ' ';

            string s = to_string(S);
            int temp = 1;
            for (int i = 0; i < s.length(); ++i)
            {
                temp *= (int)s[i] - '0';
            }
            S = temp;
        }
        cout << S << '\n';
    }

    return 0;
}
