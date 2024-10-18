import sys

sys.stdin = open('input.txt')

T = int(input())


def dfs_recursive(cnt, r):
    for c in range(cnt):
        if grid[r][c] == 1 and not visited[c]:
            visited[c] = True
            print(c, end=' ')
            order_visit.append(c)
            dfs_recursive(cnt, c)


for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    isvisited = []
    order_visit = [0]

    # 첫 번째 정점 방문
    visited[0] = True
    print(f'#{tc}', end=' ')
    print(order_visit[0], end=' ')
    dfs_recursive(N, 0)
    print()

