#include <iostream>

using namespace std;

string S, explosive;
string result = "";

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> S >> explosive;
    int exp_len = explosive.length();

    for (char c : S)
    {
        result.push_back(c);

        if (result.size() >= exp_len)
        {
            bool is_explode = true;
            for (int i = exp_len - 1; i >= 0; --i)
            {
                if (!(result[result.size() - exp_len + i] == explosive[i]))
                {
                    is_explode = false;
                    break;
                }
            }
            if (is_explode)
                result.resize(result.size() - exp_len);
        }
    }

    cout << (result.empty() ? "FRULA" : result);

    return 0;
}
