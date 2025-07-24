#include <iostream>
#include <stack>
#include <tuple>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int i = 0;
    int j = 0;
    int columns = 0;
    int diagonal = 0;
    int antidiagonal = 0;

    stack<tuple<int, int, int, int, int>> s;
    s.push(make_tuple(i, j, columns, diagonal, antidiagonal));

    int count = 0;

    while (!s.empty())
    {
        tuple<int, int, int, int, int> c = s.top();
        s.pop();

        i = get<0>(c);
        j = get<1>(c);
        columns = get<2>(c);
        diagonal = get<3>(c);
        antidiagonal = get<4>(c);

        while (i < N && j < N)
        {
            if (columns ^ (1 << j) && diagonal ^ (1 << (i - j + N - 1)) && antidiagonal ^ (1 << (i + j)))
            {
                if (i == N - 1)
                {
                    cout << i << ' ' << j << ' ' << '\n';
                    ++count;
                }
                else
                {
                    s.push(make_tuple(i, j + 1, columns, diagonal, antidiagonal));
                    columns |= 1 << j;
                    diagonal |= 1 << (i - j + N - 1);
                    antidiagonal |= 1 << (i + j);
                    i += 1;
                    j = -1;
                    break;
                }
            }
            ++j;
        }
    }
    cout << count;
    return 0;
}
