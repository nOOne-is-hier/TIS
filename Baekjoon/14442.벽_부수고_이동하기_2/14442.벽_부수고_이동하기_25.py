import sys
from collections import deque

sys.stdin = open('input.txt')

# 델타 배열 (상, 하, 좌, 우 이동을 위한 방향)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 입력 처리
N, M, K = map(int, input().split())
game_map = [list(map(int, input().strip())) for _ in range(N)]

# 방문 처리 배열 (각 좌표에서 벽을 부순 횟수에 따라 방문 여부를 관리하는 비트마스크)
visited = [[0] * M for _ in range(N)]

# BFS 탐색을 위한 큐
order = deque([(0, 0, 0, 1)])  # (row, column, 부순 벽의 수, step)
visited[0][0] = 1 << 0  # 시작점에서 벽을 부수지 않은 상태로 방문 처리

is_arrived = False  # 탐색 성공 여부 플래그

# BFS 탐색 시작
while order:
    r, c, broken_blocks, step = order.popleft()

    # 종료 조건: (N-1, M-1) 도착
    if r == N - 1 and c == M - 1:
        print(step)
        is_arrived = True
        break

    # 상하좌우 탐색
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 맵의 범위를 벗어나지 않고, 이전 상태를 재탐색하지 않도록 조건 추가
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] & ((1 << broken_blocks + 1) - 1):
            # 빈 칸(0)을 이동하는 경우
            if game_map[nr][nc] == 0:
                visited[nr][nc] |= (1 << broken_blocks)  # 현재 벽 부순 횟수를 기록
                order.append((nr, nc, broken_blocks, step + 1))

            # 벽(1)을 만난 경우, 벽을 부술 수 있는지 확인
            elif game_map[nr][nc] == 1 and broken_blocks < K and not (visited[nr][nc] & (1 << (broken_blocks + 1))):
                visited[nr][nc] |= (1 << (broken_blocks + 1))  # 벽을 부순 후 방문 처리
                order.append((nr, nc, broken_blocks + 1, step + 1))

# 완주하지 못했을 경우
if not is_arrived:
    print(-1)
