// Is it a Number? (11145)
// https://www.acmicpc.net/problem/11145

#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, l, r;
    cin >> T;
    cin.ignore();

    while (T--)
    {
        string line, buffer = "";
        getline(cin, line);

        l = 0;
        r = line.length() - 1;

        while (l < r && isspace(line[l]))
            ++l;
        while (l < r && isspace(line[r]))
            --r;

        for (int i = l; i <= r; ++i)
            if (!isdigit(line[i]))
            {
                buffer = "invalid input";
                break;
            }

        while (l < r && line[l] == '0')
            ++l;
        buffer = buffer.length() ? buffer : line.substr(l, r - l + 1);

        cout << buffer << '\n';
    }
    return 0;
}