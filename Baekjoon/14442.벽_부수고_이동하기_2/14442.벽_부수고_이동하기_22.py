import sys
from collections import deque

sys.stdin = open('input.txt')

# 델타 배열 (상, 하, 좌, 우 이동을 위한 방향)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 입력 처리
N, M, K = map(int, input().split())
game_map = [list(map(int, input().strip())) for _ in range(N)]

# 방문 처리 배열 (3차원 배열)
# visited[r][c][1][k] => (r, c) 위치에서 k개의 벽을 부순 상태에서의 방문 여부
is_visited = [[[K + 1, [False] * (K + 1)] for _ in range(M)] for _ in range(N)]

# BFS 탐색을 위한 큐
order = deque([(0, 0, 0, 1)])  # (row, column, 부순 벽의 수, step)
is_visited[0][0][0] = 0
is_visited[0][0][1][0] = True  # 시작점 방문 처리

is_arrived = False
# 탐색 시작
while order:
    r, c, broken_blocks, step = order.popleft()

    # 종료 조건: (N-1, M-1) 도착
    if r == N - 1 and c == M - 1:
        print(step)
        break

    # 상하좌우 탐색
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]

        # 종료 조건: (N-1, M-1) 도착
        if nr == N - 1 and nc == M - 1:
            print(step + 1)
            is_arrived = True
            break

        # 맵의 범위를 벗어나지 않는지 확인
        # 이전 상태에서 탐색한 곳은 재탐색 하지 않음, 그러나 다음 상태가 탐색한 곳은 탐색
        if 0 <= nr < N and 0 <= nc < M and broken_blocks < is_visited[nr][nc][0]:
            # 빈 칸(0)을 이동하는 경우
            if game_map[nr][nc] == 0 and not is_visited[nr][nc][1][broken_blocks]:
                is_visited[nr][nc][0] = min(is_visited[nr][nc][0], broken_blocks)
                is_visited[nr][nc][1][broken_blocks] = True
                order.append((nr, nc, broken_blocks, step + 1))

            # 벽(1)을 만난 경우, 벽을 부술 수 있는지 확인
            elif game_map[nr][nc] == 1 and broken_blocks < K and not is_visited[nr][nc][1][broken_blocks + 1]:
                is_visited[nr][nc][0] = min(is_visited[nr][nc][0], broken_blocks)
                is_visited[nr][nc][1][broken_blocks + 1] = True
                order.append((nr, nc, broken_blocks + 1, step + 1))

    if is_arrived:
        break

# 완주하지 못했을 경우
else:
    print(-1)
