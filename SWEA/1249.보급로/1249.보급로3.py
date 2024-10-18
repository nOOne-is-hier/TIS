import sys
from collections import deque

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    ardennes = [list(map(int, list(input().strip()))) for _ in range(N)]

    # 방문처리를 위한 배열을 최대 비용으로 초기화
    max_cost = N ** 2 * 9
    is_visited = [[max_cost] * N for _ in range(N)]
    orders = deque([(0, 0)])
    is_visited[0][0] = ardennes[0][0]

    # 4방위 이동
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # BFS 시작
    while orders:
        r, c = orders.popleft()
        current_cost = is_visited[r][c]

        # 4방위로 이동
        for dir in range(4):
            nr, nc = r + dr[dir], c + dc[dir]
            if 0 <= nr < N and 0 <= nc < N:
                next_cost = current_cost + ardennes[nr][nc]
                if next_cost < is_visited[nr][nc]:
                    is_visited[nr][nc] = next_cost
                    orders.append((nr, nc))

    print(f'#{tc} {is_visited[N - 1][N - 1]}')
