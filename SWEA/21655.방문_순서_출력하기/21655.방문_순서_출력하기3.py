import sys

sys.stdin = open('input.txt')

T = int(input())


def dfs_recursive(cnt, r=0):
    for c in range(cnt):
        if grid[r][c] == 1 and not c in order_visit:
            grid[r][c] = 0
            print(c, end=' ')
            isvisited.append(r)
            order_visit.append(c)
            dfs_recursive(cnt, c)

    if isvisited:
        dfs_recursive(cnt, isvisited.pop())
    else:
        return

for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    isvisited = []
    order_visit = [0]
    print(f'#{tc}', end=' ')
    print(order_visit[0], end=' ')
    dfs_recursive(N)
    print()