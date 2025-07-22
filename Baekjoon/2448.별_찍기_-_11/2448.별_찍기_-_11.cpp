#include <iostream>
#include <vector>

using namespace std;

int N;
vector<vector<int>> stars;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;

    stars.assign(N, vector<int>(N * 2 - 1, 0));

    // 바닥 채우기
    for (int i = 0; i < N * 2 - 1; ++i)
    {
        if (i < 5)
            stars[N - 1][i] = 1;
        else
        {
            int lasts = 0;
            for (int j = 1; j <= 5; ++j)
                lasts += stars[N - 1][i - j];
            lasts <= 4 ? stars[N - 1][i] = 1 : stars[N - 1][i] = 0;
        }
    }

    // N - 2 부터 순회 시작
    for (int i = N - 2; i >= 0; --i)
        for (int j = 0; j < N * 2 - 1; ++j)
        {
            if (i % 3 == 0)
                if (0 < j && j < N * 2 - 2)
                    if (stars[i + 1][j - 1] == 1 && stars[i + 1][j + 1] == 1 && stars[i + 1][j] == 0)
                        stars[i][j] = 1;
            if (i % 3 == 1)
                if (0 < j && j < N * 2 - 2)
                    if (stars[i + 1][j - 1] == 1 && stars[i + 1][j] == 1 && stars[i + 1][j + 1] == 1 && stars[i][j - 1] == 0)
                        stars[i][j] = 1;
            if (i % 3 == 2)
                if (0 < j && j < N * 2 - 2)
                    if (stars[i + 1][j - 1] == 1)
                    {
                        while (stars[i + 1][j] != 1)
                        {
                            if (j < 5)
                                stars[i][j] = 1;
                            else
                            {
                                int lasts = 0;
                                for (int k = 1; k <= 5; ++k)
                                    lasts += stars[i][j - k];
                                lasts <= 4 ? stars[i][j] = 1 : stars[i][j] = 0;
                            }
                            ++j;
                        }
                        ++j;
                    }
        }

    for (vector<int> &row : stars)
    {
        for (int &star : row)
            cout << ((star == 0) ? ' ' : '*');
        cout << '\n';
    }
    return 0;
}
