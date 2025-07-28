#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, N;
    cin >> R;

    char history[R + 1];

    cin >> history >> N;

    char opponent_history[N][R + 1];

    for (int i = 0; i < N; ++i)
        cin >> opponent_history[i];

    int result = 0;
    int best = 0;
    for (int j = 0; j < R; ++j)
    {
        int case1 = 0;
        int case2 = 0;
        int case3 = 0;

        for (int i = 0; i < N; ++i)
        {
            if (opponent_history[i][j] == history[j])
                ++result;
            if (opponent_history[i][j] == 'R')
            {
                if (history[j] == 'P')
                    result += 2;
                case2 += 1;
                case3 += 2;
            }
            if (opponent_history[i][j] == 'P')
            {
                if (history[j] == 'S')
                    result += 2;
                case3 += 1;
                case1 += 2;
            }
            if (opponent_history[i][j] == 'S')
            {
                if (history[j] == 'R')
                    result += 2;
                case1 += 1;
                case2 += 2;
            }
        }
        best += max(case1, max(case2, case3));
    }

    cout << result << '\n'
         << best;

    return 0;
}
