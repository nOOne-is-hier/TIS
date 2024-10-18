import sys
sys.stdin = open('input.txt')


def check(row, column):

    for r in range(row):
        if is_visited[r][column]:
            return False

    nr, nc = row - 1, column - 1
    while nr >= 0 and nc >= 0:
        if is_visited[nr][nc]:
            return False
        nr -= 1
        nc -= 1

    for nr, nc in zip(range(row - 1, -1, -1), range(column + 1, N)):
        if is_visited[nr][nc]:
            return False

    return True


def dfs(row):
    global n_queen
    if row == N:
        n_queen += 1
        return

    for column in range(N):
        if check(row, column):
            is_visited[row][column] = 1
            dfs(row + 1)
            is_visited[row][column] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    is_visited = [[0] * N for _ in range(N)]
    n_queen = 0

    dfs(0)
    print(f'#{tc} {n_queen}')
