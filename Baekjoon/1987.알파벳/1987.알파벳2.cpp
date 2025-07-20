#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int R, C;
vector<string> board;
int result = 0;
int dr[] = {-1, 0, 1, 0};
int dc[] = {0, 1, 0, -1};

vector<vector<unordered_set<int>>> memo;

void dfs(int r, int c, int visited, int dist)
{
    if (dist == 26)
    {
        cout << 26;
        exit(0);
    }

    if (result < dist)
        result = dist;

    for (int dir = 0; dir < 4; ++dir)
    {
        int nr = r + dr[dir];
        int nc = c + dc[dir];

        if (0 <= nr && nr < R && 0 <= nc && nc < C)
        {
            int ch = board[nr][nc] - 'A';
            int next_mask = visited | (1 << ch);

            if (!(visited & (1 << ch)) && !memo[nr][nc].count(next_mask))
            {
                memo[nr][nc].insert(next_mask);
                dfs(nr, nc, next_mask, dist + 1);
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> R >> C;
    board.resize(R);
    for (string &row : board)
        cin >> row;

    memo.assign(R, vector<unordered_set<int>>(C));

    int start_char = board[0][0] - 'A';
    int init_mask = 1 << start_char;
    memo[0][0].insert(init_mask);
    dfs(0, 0, init_mask, 1);

    cout << result;

    return 0;
}