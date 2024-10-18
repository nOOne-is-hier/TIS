import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def is_safe(r, c):

    if is_visited[r][c] or minesweeper[r][c] == '*':
        is_visited[r][c] = 1
        return False

    for dir in range(8):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N:
            if minesweeper[nr][nc] == '*':
                is_visited[nr][nc] = 1
                return False

    return True

def dfs(r, c):
    coordinates = [(r, c)]
    while coordinates:
        lr, lc = coordinates.pop()
        is_visited[lr][lc] = 1
        minesweeper[lr][lc] = '0'

        for dir in range(8):
            nr = lr + dr[dir]
            nc = lc + dc[dir]
            if 0 <= nr < N and 0 <= nc < N and not is_visited[nr][nc]:
                if is_safe(nr, nc):
                    coordinates.append((nr, nc))
                else:
                    is_visited[nr][nc] = 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    minesweeper = [list(input()) for _ in range(N)]
    is_visited = [[0]*N for _ in range(N)]

    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]
    click = 0

    for r in range(N):
        for c in range(N):
            if is_safe(r, c) and not is_visited[r][c]:
                click += 1
                dfs(r, c)

    for r in range(N):
        for c in range(N):
            if minesweeper[r][c] != '*' and not is_visited[r][c]:
                click += 1

    print(f'#{tc} {click}')