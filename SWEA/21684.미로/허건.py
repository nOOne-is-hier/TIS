def dfs(x, y):
    if maze[y][x] == "2":  # 출구 발견
        return True
    if maze[y][x] == "1":  # 벽
        return False

    maze[y][x] = "1"  # 방문 표시

    # 상하좌우 탐색
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and maze[ny][nx] != "1":
            if dfs(nx, ny):
                return True

    return False

import sys
import time
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    maze = [list(input().strip()) for _ in range(N)]

    # 출발점 찾기
    start_x = start_y = -1
    for j in range(N):
        for i in range(N):
            if maze[j][i] == "3":
                start_x, start_y = i, j
                break
        if start_x != -1:
            break
    start_time = time.time()

    if dfs(start_x, start_y):
        print(f"#{_ + 1} {1}")  # 출구에 도달
    else:
        print(f"#{_ + 1} {0}")  # 출구에 도달하지 못함
    end_time = time.time()

    execution_time = end_time - start_time

    print(f'Execution Time: {execution_time:.6f} seconds')