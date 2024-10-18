import sys
from collections import deque

sys.stdin = open('input.txt')

class DefaultCount(int):
    def __str__(self):
        return '-1'

# 델타 배열
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 낮과 밤
day_night_patter = ('DAY', 'NIGHT')

# 입력
N, M, K = map(int, input().split())
map_info = [input() for _ in range(N)]
over_limit = DefaultCount(1000000)
is_visited = [[[K + 1, over_limit] for _ in range(M)] for _ in range(N)]

order = deque([(0, 0, 0, 1)])   # row, column, broken walls, steps
is_visited[0][0][0] = 0

while order:
    row, col, broken_walls, steps = order.popleft()

    # 최소 비용 탐색
    if row == N - 1 and col == M - 1:
        is_visited[row][col][1] = min(steps, is_visited[row][col][1])
        continue

    for dir in range(4):
        nr = row + dr[dir]
        nc = col + dc[dir]

        # 경계 설정, 벽을 부순 횟수 기준 백트래킹
        if 0 <= nr < N and 0 <= nc < M and broken_walls < is_visited[nr][nc][0]:
            if map_info[nr][nc] == '0':
                is_visited[nr][nc][0] = broken_walls
                order.append((nr, nc, broken_walls, steps + 1))
            # 벽을 부술 수 있는 횟수가 남아 있는가 / 한 개 더 부쉈을 때 기준으로 백트래킹
            elif map_info[nr][nc] == '1' and broken_walls < K and broken_walls + 1 < is_visited[nr][nc][0]:
                if steps % 2 == 1:  # 낮이라면
                    is_visited[nr][nc][0] = broken_walls + 1
                    order.append((nr, nc, broken_walls + 1, steps + 1))
                else:   # 밤이라면
                    order.append((row, col, broken_walls, steps + 1))
print(is_visited[N - 1][M - 1][1])