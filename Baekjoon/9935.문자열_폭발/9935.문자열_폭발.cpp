#include <iostream>
#include <list>

using namespace std;

string S, explosive;
list<char> l;
int S_len;
int exp_len;

void simulation(char c)
{
    l.push_back(c);
    if (c == explosive[exp_len - 1] && l.size() >= exp_len - 1)
    {
        int count = exp_len;
        list<char>::iterator it = l.end();
        while (count)
        {
            --count;
            --it;

            if (explosive[count] != *it)
                break;

            if (!count)
            {
                l.erase(it, l.end());
                return;
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> S >> explosive;
    S_len = S.length();
    exp_len = explosive.length();

    for (char c : S)
        simulation(c);

    if (l.empty())
        cout << "FRULA";
    else
    {
        for (char c : l)
            cout << c;
    }
    return 0;
}
