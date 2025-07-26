#include <iostream>

using namespace std;

int N, i, j, k;
long B;
int matrix[5][5], result[5][5], temp[5][5];

void multiplication(int a[5][5], int b[5][5])
{
    for (i = 0; i < N * N; ++i)
        temp[i / N][i % N] = 0;

    for (i = 0; i < N; ++i)
        for (k = 0; k < N; ++k)
            for (j = 0; j < N; ++j)
                temp[i][j] += a[i][k] * b[k][j];

    for (i = 0; i < N * N; ++i)
        a[i / N][i % N] = temp[i / N][i % N] % 1'000;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> B;

    for (; i < N; ++i)
        for (j = 0; j < N; cin >> matrix[i][j], matrix[i][j] %= 1'000, ++j)
            result[i][j] = (i == j);

    for (; B; B >>= 1)
    {
        if (B % 2 == 1)
            multiplication(result, matrix);
        multiplication(matrix, matrix);
    }

    for (i = 0; i < N; ++i, cout << '\n')
        for (j = 0; j < N; ++j)
            cout << result[i][j] << ' ';
    return 0;
}
