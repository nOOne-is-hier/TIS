#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int N;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;

    vector<vector<int>> board(2, vector<int>(3));
    vector<vector<int>> maxBoard(2, vector<int>(3, -1));
    vector<vector<int>> minBoard(2, vector<int>(3, 1e9));

    for (int r = 0; r < N; ++r)
    {
        for (int &score : board[r % 2])
            cin >> score;
        for (int c = 0; c < 3; ++c)
            for (int d = 0; d < 3; ++d)
            {
                maxBoard[r % 2][c] = r > 0 ? ((0 <= c - d + 1 && c - d + 1 < 3 && maxBoard[r % 2][c] < maxBoard[(r - 1) % 2][c - d + 1] + board[r % 2][c]) ? maxBoard[(r - 1) % 2][c - d + 1] + board[r % 2][c] : maxBoard[r % 2][c]) : board[r % 2][c];
                minBoard[r % 2][c] = r > 0 ? ((0 <= c - d + 1 && c - d + 1 < 3 && minBoard[r % 2][c] > minBoard[(r - 1) % 2][c - d + 1] + board[r % 2][c]) ? minBoard[(r - 1) % 2][c - d + 1] + board[r % 2][c] : minBoard[r % 2][c]) : board[r % 2][c];
            }

        board[(r + 1) % 2] = vector<int>(3);
        maxBoard[(r + 1) % 2] = vector<int>(3, -1);
        minBoard[(r + 1) % 2] = vector<int>(3, 1e9);
    }
    cout << (N % 2 == 0 ? *max_element(maxBoard.back().begin(), maxBoard.back().end()) : *max_element(maxBoard.front().begin(), maxBoard.front().end())) << ' ' << (N % 2 == 0 ? *min_element(minBoard.back().begin(), minBoard.back().end()) : *min_element(minBoard.front().begin(), minBoard.front().end()));

    return 0;
}
