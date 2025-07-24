#include <iostream>

using namespace std;

int N;
int columns = 0;
int diagonal = 0;
int antidiagonal = 0;
int result = 0;

void dfs(int r, int columns, int diagonal, int antidiagonal)
{
    if (r == N)
    {
        ++result;
        return;
    }

    for (int c = 0; c < N; ++c)
    {
        if ((columns & (1 << c)) == 0 && (diagonal & (1 << (r - c + N - 1))) == 0 && (antidiagonal & (1 << (r + c))) == 0)
            dfs(r + 1, columns | (1 << c), diagonal | (1 << (r - c + N - 1)), antidiagonal | (1 << (r + c)));
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;

    dfs(0, 0, 0, 0);

    cout << result;

    return 0;
}
