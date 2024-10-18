import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')

class DefaultCount(int):
    def __str__(self):
        return '-1'

# 델타 배열
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 입력
N, M, K = map(int, input().split())
map_info = [input() for _ in range(N)]
over_limit = DefaultCount(1000000)
is_visited = [[[over_limit] * (K + 1) for _ in range(M)] for _ in range(N)]

order = [(0, 0, 0, 1)]   # broken walls, row, column, steps
is_visited[0][0][0] = 0

while order:
    broken_walls, row, col, steps = heappop(order)

    for dir in range(4):
        nr = row + dr[dir]
        nc = col + dc[dir]

        # 경계 설정, 벽을 부순 횟수 기준 백트래킹
        if 0 <= nr < N and 0 <= nc < M and steps < is_visited[nr][nc][broken_walls]:
            if map_info[nr][nc] == '0':
                is_visited[nr][nc][broken_walls] = steps
                heappush(order, (broken_walls, nr, nc, steps + 1))
            # 벽을 부술 수 있는 횟수가 남아 있는가 / 한 개 더 부쉈을 때 기준으로 백트래킹
            elif map_info[nr][nc] == '1' and broken_walls < K and steps < is_visited[nr][nc][broken_walls + 1]:
                if steps % 2 == 1:  # 낮이라면
                    is_visited[nr][nc][broken_walls + 1] = steps
                    heappush(order, (broken_walls + 1, nr, nc, steps + 1))
                else:   # 밤이라면
                    heappush(order, (broken_walls, row, col, steps + 1))

tep_max = 0
for num in is_visited[N - 1][M - 1]:
    if num != over_limit:
        tep_max = max(num, tep_max)

if tep_max:
    print(tep_max + 1)
else:
    print(over_limit)
