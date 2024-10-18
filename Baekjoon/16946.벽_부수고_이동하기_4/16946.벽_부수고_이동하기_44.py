import sys
from collections import deque
sys.stdin = open('input.txt')

# 델타 배열
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def BFS(row, col):

    order = deque([(row, col)])
    is_visited[row][col] = True
    count_movable = 1

    while order:
        r, c = order.popleft()

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < N and 0 <= nc < M and not is_visited[nr][nc]:
                is_visited[nr][nc] = True
                if map_info[nr][nc] == 0:
                    count_movable += 1
                    order.append((nr, nc))
                elif map_info[nr][nc] != 0:
                    log.append((nr, nc))

    return count_movable


N, M = map(int, input().split())
map_info = [list(map(int, input().strip())) for _ in range(N)]
is_visited = [[False] * M for _ in range(N)]
log = deque()

for r in range(N):
    for c in range(M):
        if map_info[r][c] == 0 and not is_visited[r][c]:
            counts = BFS(r, c)
            while log:
                row, col = log.popleft()
                map_info[row][col] += counts
                is_visited[row][col] = False

for r in range(N):
    for c in range(M):
        print(map_info[r][c] % 10, end='')
    print()
