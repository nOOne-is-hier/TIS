import sys
sys.stdin = open('input.txt')

def is_safe(n, r, c, board):
    copy_board = [row[:] for row in board]

    for dir in range(4):
        dis = 0
        while True:
            nr = r + (dr[dir] * dis)
            nc = c + (dc[dir] * dis)
            if 0 <= nr < n and 0 <= nc < n:
                if not copy_board[nr][nc] or copy_board[nr][nc] == 2:
                    copy_board[nr][nc] = 2
                    dis += 1
                    continue
                else:
                    return False
            else:
                break
    return copy_board

def dfs(n, row=0, column=0, board=None, n_queen=0, cases=None):
    if not cases:
        cases = [0]

    if n_queen == n:
        cases[0] += 1
        return

    if not board:
        board = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if (r == row and column <= c) or row < r:
                if not board[r][c]:
                    copy_board = is_safe(n, r, c, board)
                    if copy_board:
                        copy_board[r][c] = 1
                        dfs(n, r, c, copy_board, n_queen + 1, cases)

    return cases[0]


for tc in range(1, int(input()) + 1):
    N = int(input())

    dr = [0, -1, -1, -1]
    dc = [-1, -1, 0, 1]

    result = dfs(N)
    print(f'#{tc} {result}')