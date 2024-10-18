import sys

sys.stdin = open('input.txt')
from collections import deque

# 델타 배열
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

class Infinite(float):
    def __str__(self):
        return 'impossible'

T = int(input())

for tc in range(1, T + 1):
    map_info = [input() for _ in range(4)]
    big_num = Infinite('INF')
    is_visited = [[big_num] * 5 for _ in range(4)]

    start = goal = None
    for r in range(4):
        for c in range(5):
            if map_info[r][c] == 'A':
                start = (r, c)
            elif map_info[r][c] == 'B':
                goal = (r, c)
            if start and goal:
                break
        if start and goal:
            break

    order = deque([start])
    is_visited[start[0]][start[1]] = 0

    while order:
        row, col = order.popleft()
        for dir in range(4):
            nr = row + dr[dir]
            nc = col + dc[dir]
            if 0 <= nr < 4 and 0 <= nc < 5:
                if map_info[nr][nc] != '#':
                    if is_visited[nr][nc] > is_visited[row][col] + 1:
                        is_visited[nr][nc] = is_visited[row][col] + 1
                        order.append((nr, nc))
    result = is_visited[goal[0]][goal[1]]
    print(f'#{tc}', result)
