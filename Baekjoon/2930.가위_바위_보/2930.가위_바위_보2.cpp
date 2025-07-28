#include <iostream>

using namespace std;

int get_score(char me, char opponent)
{
    if (me == opponent)
        return 1;
    if ((me == 'R' && opponent == 'S') ||
        (me == 'S' && opponent == 'P') ||
        (me == 'P' && opponent == 'R'))
        return 2;
    return 0;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, N;
    cin >> R;
    char sanggeun[R + 1];
    cin >> sanggeun >> N;
    char friends[N][R + 1];
    for (int i = 0; i < N; ++i)
        cin >> friends[i];

    int actual_score = 0;
    for (int j = 0; j < R; ++j)
        for (int i = 0; i < N; ++i)
            actual_score += get_score(sanggeun[j], friends[i][j]);

    int max_score = 0;
    const string moves = "RSP";
    for (int j = 0; j < R; ++j)
    {
        int round_best = 0;
        for (char move : moves)
        {
            int temp = 0;
            for (int i = 0; i < N; ++i)
                temp += get_score(move, friends[i][j]);
            round_best = max(round_best, temp);
        }
        max_score += round_best;
    }

    cout << actual_score << '\n'
         << max_score;

    return 0;
}
