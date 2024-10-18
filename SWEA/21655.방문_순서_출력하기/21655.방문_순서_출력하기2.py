import sys
sys.stdin = open('input.txt')

def dfs(node):
    print(node, end=' ')

    for i in range(N):
        if grid[node][i] == 0 or visited[i]:
            continue

        visited[i] = 1 # 방문처리
        dfs(i)

'''def dfs_stack(start):
    stack = [start]

    while stack:
        now = stack.pop()

        print(now, end=' ')

        for i in range(N-1, -1, -1):
            if grid[now][i] == 0 or visited[i]:
                continue

            visited[i] = 1
            stack.append(i)'''


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1 # 출발점
    print(f'#{tc}', end=' ')
    dfs(0)
    print()

    # print(f'#{tc}', end=' ')
    # dfs_stack(0)
    # print()