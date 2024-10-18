import sys

sys.stdin = open('input.txt')

from heapq import heappush, heappop

# 델타 배열
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
rooms = [input() for _ in range(N)]
is_visited = [[2500] * N for _ in range(N)]

if rooms[0][0] == '1':
    start = (0, 0, 0)
else:
    start = (-1, 0, 0)
order = [(start)]
is_visited[0][0] = -start[0]    # 방을 바꾼 횟수

while order:
    count_conversion, row, col = heappop(order)
    count_conversion = -count_conversion

    for dir in range(4):
        nr = row + dr[dir]
        nc = col + dc[dir]

        if 0 <= nr < N and 0 <= nc < N:
            if rooms[nr][nc] == '1' and count_conversion < is_visited[nr][nc]:
                is_visited[nr][nc] = count_conversion
                heappush(order, (-count_conversion, nr, nc))
            elif rooms[nr][nc] == '0' and count_conversion + 1 < is_visited[nr][nc]:
                is_visited[nr][nc] = count_conversion + 1
                heappush(order, (-count_conversion - 1, nr, nc))

print(is_visited[N - 1][N - 1])
