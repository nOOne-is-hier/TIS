import sys
import time
from collections import deque

sys.stdin = open('input.txt')


# 미로를 탐색하는 반복 함수
def escape_maze(start_r, start_c):
    stack = deque([(start_r, start_c)])
    crossroads = []

    while stack:
        r, c = stack.pop()
        maze[r][c] = 1

        direction = -1
        iscrossroads = 0

        for idx in range(4):
            nr, nc = r + dr[idx], c + dc[idx]
            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == 3:
                    return True
                elif maze[nr][nc] == 0:
                    iscrossroads += 1
                    direction = idx

        if iscrossroads >= 2:
            crossroads.append((r, c))

        if iscrossroads == 0 and not crossroads:
            continue

        if iscrossroads == 0 and crossroads:
            nr, nc = crossroads.pop()
            stack.append((nr, nc))
        else:
            stack.append((r + dr[direction], c + dc[direction]))

    return False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    # 델타 좌표
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 시작·도착 좌표 탐색
    start_r = start_c = -1

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start_r = r
                start_c = c
                break
        if start_r != -1:
            break

    # 시작 시간 측정
    start_time = time.time()

    result = escape_maze(start_r, start_c)

    # 종료 시간 측정
    end_time = time.time()

    # 실행 시간 계산
    execution_time = end_time - start_time
    print(f'#{tc} {int(result)}')
    print(f'Execution Time: {execution_time:.6f} seconds')
