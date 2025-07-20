#include <iostream>
#include <vector>

using namespace std;

int R, C;
bool is_visited[26];
vector<string> board;
pair<int, int> delta[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
int max_dist = 0;

void dfs(int r, int c, int dist)
{
    if (dist == 26)
    {
        cout << 26;
        exit(0);
    }

    if (max_dist < dist)
        max_dist = dist;

    for (pair<int, int> &dir : delta)
    {
        int nr = r + dir.first;
        int nc = c + dir.second;

        if (0 <= nr && nr < R && 0 <= nc && nc < C && !is_visited[board[nr][nc] - 'A'])
        {
            is_visited[board[nr][nc] - 'A'] = true;
            dfs(nr, nc, dist + 1);
            is_visited[board[nr][nc] - 'A'] = false;
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

    is_visited[board[0][0] - 'A'] = true;
    dfs(0, 0, 1);

    cout << max_dist;

    return 0;
}
