#include <iostream>

using namespace std;

string s;
int dat[26];
int max_c = 0;
int max_i;
int count = 0;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> s;

    for (char &c : s)
    {
        c <= 'Z' ? (dat[c - 'A'] += 1) : (dat[c - 'a'] += 1);
    }

    for (int i = 0; i < 26; ++i)
    {
        if (max_c < dat[i])
        {
            max_c = dat[i];
            max_i = i;
            count = 1;
        }
        else if (max_c == dat[i])
            ++count;
    }

    cout << (count == 1 ? (char)(max_i + 'A') : '?');

    return 0;
}
