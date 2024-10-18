import sys
from collections import deque
sys.stdin = open('input.txt')

# 델타 배열
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 입력
N, M, K = map(int, input().split())
# 각 상태를 구분하기 위한 배열
game_map = [[{int(char)} for char in input().strip()] for _ in range(N)]

# 탐색
order = deque([(0, 0, 0, 1)])   # 시작점 (row, column, 부순 벽의 수, step)
game_map[0][0] |= {-1, 2}   # 시작점 방문처리
is_arrived = False  # 완주 여부

# 탐색 시작
while order:
    r, c, broken_blocks, step = order.popleft()
    # 종료조건
    if r == N - 1 and c == M - 1:
        print(step)
        is_arrived = True
        break
    # 이동할 좌표
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        # 0 빈 필드, 1 벽 / 초기값, set에 0이 있다면 통로, 1이 있다면 벽
        # -1 부순 벽이 0일 때의 방문처리
        # 2 ~ 2 + K + 1 0과 1에 방문처리
        # 맵을 벗어나지 말 것
        if 0 <= nr < N and 0 <= nc < M:
            diff = game_map[nr][nc] - {-1, 0, 1}
            if not diff or (len(diff) > 0 and broken_blocks + 1 < min(diff)):
                # 통로에 대한 방문처리
                if 0 in game_map[nr][nc]:
                    if -1 not in game_map[nr][nc] and broken_blocks == 0:
                        game_map[nr][nc].add(-1)
                        order.append((nr, nc, broken_blocks, step + 1))
                    elif broken_blocks > 0:
                        game_map[nr][nc].add(broken_blocks + 1)
                        order.append((nr, nc, broken_blocks, step + 1))
                # 벽에 대한 방문처리
                elif 1 in game_map[nr][nc]:
                    if broken_blocks < K:   # K번 벽을 부쉈다면 더 이상 벽을 부술 수 없음
                        game_map[nr][nc].add(broken_blocks + 2) # 방문처리
                        order.append((nr, nc, broken_blocks + 1, step + 1))
# 완주에 실패 했다면
if not is_arrived:
    print(-1)