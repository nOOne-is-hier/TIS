import sys
from collections import deque
sys.stdin = open('input.txt')

# 델타 배열
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def BFS(row, col):

    cells_to_move = 1
    order = deque([(row, col)])

    while order:
        r, c = order.popleft()

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < N and 0 <= nc < M:
                if map_info[nr][nc] == '0' and is_visited[nr][nc] != count_wall:
                    order.append((nr, nc))
                    is_visited[nr][nc] = count_wall
                    cells_to_move += 1

    return cells_to_move % 10

N, M = map(int, input().split())
map_info = [input() for _ in range(N)]
is_visited = [[0] * M for _ in range(N)]

count_wall = 0
for r in range(N):
    for c in range(M):
        if map_info[r][c] == '0':
            print('0', end='')
        elif map_info[r][c] == '1':
            count_wall += 1
            cells = BFS(r, c)
            print(cells, end='')
    print()