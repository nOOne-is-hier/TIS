#include <iostream>
#include <vector>

using namespace std;

int N;
long B;
vector<vector<int>> matrix;

vector<vector<int>> multiplication(vector<vector<int>> a, vector<vector<int>> b)
{
    vector<vector<int>> result(N, vector<int>(N));

    for (int i = 0; i < N; ++i)
        for (int k = 0; k < N; ++k)
            for (int j = 0; j < N; ++j)
                result[i][j] = (result[i][j] + (a[i][k] * b[k][j])) % 1'000;

    return result;
}

vector<vector<int>> dnq(long pow)
{
    if (pow == 1)
        return matrix;

    vector<vector<int>> half = dnq(pow / 2);
    vector<vector<int>> result = multiplication(half, half);

    if (pow % 2 == 1)
        result = multiplication(result, matrix);

    return result;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> B;

    matrix.resize(N, vector<int>(N));
    for (vector<int> &row : matrix)
        for (int &elem : row)
            cin >> elem, elem %= 1'000;

    vector<vector<int>> result = dnq(B);
    for (vector<int> &row : result)
    {
        for (int &elem : row)
            cout << elem << ' ';
        cout << '\n';
    }

    return 0;
}
