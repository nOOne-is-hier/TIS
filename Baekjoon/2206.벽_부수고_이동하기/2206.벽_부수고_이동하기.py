import sys
from collections import deque
sys.stdin = open('input.txt')

# 델타 배열
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 입력
N, M = list(map(int, input().split()))
game_map = [list(map(int, input().strip())) for _ in range(N)]

# 탐색
order = deque([(0, 0, False, 1)])
is_arrived = False

while order:
    r, c, is_broke, step = order.popleft()
    # 종료조건
    if r == N - 1 and c == M - 1:
        print(step)
        is_arrived = True
        break
    # 이동할 좌표
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        # 맵을 벗어나지 말 것
        if 0 <= nr < N and 0 <= nc < M and game_map[nr][nc] != [2, 2]:   # 2는 방문처리
            # 벽을 한 번 부숴본다
            if not is_broke:
                if game_map[nr][nc] == 1:
                    is_broke = True
                game_map[nr][nc] = 2
                order.append((nr, nc, is_broke, step + 1))
            else:
                if game_map[nr][nc] == 0:
                    game_map[nr][nc] = 2
                    order.append((nr, nc, is_broke, step + 1))

if not is_arrived:
    print(-1)