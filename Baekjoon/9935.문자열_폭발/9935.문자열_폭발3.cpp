#include <iostream>

using namespace std;

char input[1'000'001];
char explosive[37];
char stack[1'000'001];
int top = 0;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> input >> explosive;

    int exp_len = 0;
    while (explosive[exp_len] != '\0')
        ++exp_len;

    for (int i = 0; input[i] != '\0'; ++i)
    {
        stack[top++] = input[i];

        if (top >= exp_len && stack[top - 1] == explosive[exp_len - 1])
        {
            bool boom = true;
            for (int j = exp_len - 2; j >= 0; --j)
            {
                if (stack[top - exp_len + j] != explosive[j])
                {
                    boom = false;
                    break;
                }
            }
            if (boom)
                top -= exp_len;
        }
    }

    stack[top] = '\0';

    cout << (top ? stack : "FRULA");

    return 0;
}
