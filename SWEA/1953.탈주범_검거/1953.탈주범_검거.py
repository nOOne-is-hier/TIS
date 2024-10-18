import sys

sys.stdin = open('input.txt')
from collections import deque

# 델타 배열
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 배관 패턴 하드코딩
Tunnels = {'1': {0, 1, 2, 3}, '2': {0, 2}, '3': {1, 3}, '4': {0, 1}, '5': {1, 2}, '6': {2, 3}, '7': {3, 0}}

T = int(input())

for tc in range(1, T + 1):
    N, M, row, col, limit = list(map(int, input().split()))
    subterranean_tunnel = [input().split() for _ in range(N)]
    is_visited = [[-1] * M for _ in range(N)]

    tracking = deque([(row, col, subterranean_tunnel[row][col])])    # row, col, type of tunnel
    is_visited[row][col] = subterranean_tunnel[row][col]
    if limit == 1:
        print(f'#{tc}', 1)
    else:
        now = 1
        reachable_tile = 1
        while now < limit:
            tracking_by_time = deque()
            while tracking:
                row, col, type_of_tunnel = tracking.popleft()
                for dir in range(4):
                    nr = row + dr[dir]
                    nc = col + dc[dir]
                    if 0 <= nr < N and 0 <= nc < M: # 범위 안에 있어야 함
                        if dir in Tunnels[type_of_tunnel]:  # 현재 터널에서 통로가 열려있어야 함
                            next_tunnel = subterranean_tunnel[nr][nc]
                            #   다음 칸이 통로이면서 해당 방향이 열려있어야 함
                            if next_tunnel != '0' and (dir + 2) % 4 in Tunnels[next_tunnel]:
                                if is_visited[nr][nc] == -1:    # 방문하지 않았어야 함
                                    tracking_by_time.append((nr, nc, next_tunnel))
                                    is_visited[nr][nc] = 1
                                    reachable_tile += 1
            now += 1
            tracking.extend(tracking_by_time)
        print(f'#{tc}', reachable_tile)
