Dimport sys
import heapq

sys.stdin = open('input.txt')
# 델타 배열 (상하좌우 이동)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 입력 처리
N, M, K = map(int, input().split())  # 첫 번째 줄에서 N, M, K 읽음
game_map = [list(map(int, input().strip())) for _ in range(N)]  # 그 다음 줄부터 게임 맵 읽음

# 우선순위 큐 (heapq 사용), 시작점은 (0, 0)에서 시작
pq = []
heapq.heappush(pq, (1, 0, 0, 0))  # (거리, row, column, 벽을 부순 횟수)

# 방문 여부와 벽을 부순 횟수를 관리하는 비트마스크 (1 << broken_blocks)
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1 << 0  # 벽을 부수지 않고 방문 처리

# BFS 탐색 시작
while pq:
    # 현재 상태를 가져옴 (거리, r, c, 벽을 부순 횟수)
    dist, r, c, broken_blocks = heapq.heappop(pq)

    # 도착 지점에 도착하면 종료
    if r == N - 1 and c == M - 1:
        print(dist)  # 시작점도 포함해서 +1
        sys.exit(0)

    # 4방향으로 이동
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        # 맵의 범위를 벗어나지 않고, 이전 상태를 재탐색하지 않도록 조건 추가
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] & ((1 << broken_blocks + 1) - 1):
            # 더 적은 벽을 부순 상태라면 탐색을 진행 (더 많이 부순 상태는 탐색하지 않음)
            # 빈 칸(0)을 이동하는 경우
            if game_map[nr][nc] == 0:
                visited[nr][nc] |= (1 << broken_blocks)  # 벽을 부수지 않은 경우 방문 처리
                heapq.heappush(pq, (dist + 1, nr, nc, broken_blocks))

            # 벽일 경우, 벽을 부술 수 있다면
            elif game_map[nr][nc] == 1 and broken_blocks < K and not (visited[nr][nc] & (1 << (broken_blocks + 1))):
                visited[nr][nc] |= (1 << (broken_blocks + 1))  # 벽을 부수고 방문 처리
                heapq.heappush(pq, (dist + 1, nr, nc, broken_blocks + 1))

# 만약 도착할 수 없다면 -1 반환
print(-1)
