import sys
import heapq
from collections import defaultdict, deque

sys.stdin = open('input.txt')

# 델타 배열
dr = [0, 1]
dc = [1, 0]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    is_visited = [[float('inf')] * N for _ in range(N)]
    priority_queue = [(0, 0, 0, None)]  # total_damage, row, column, last_position
    logs = defaultdict(lambda: defaultdict(list))
    logs[(0, 0)][0].append(None)
    is_visited[0][0] = 0

    while priority_queue:
        total_damage, row, col, last_position = heapq.heappop(priority_queue)

        # 종료 조건 (최소 비용으로 목적지에 도달한 경우)
        if row == col == N - 1:
            break

        for dir in range(2):
            nr = row + dr[dir]
            nc = col + dc[dir]
            if 0 <= nr < N and 0 <= nc < N:
                new_damage = total_damage + field[nr][nc]
                if new_damage < is_visited[nr][nc]:
                    new_position = (nr, nc)
                    is_visited[nr][nc] = new_damage
                    heapq.heappush(priority_queue, (new_damage, nr, nc, (row, col)))
                    logs[new_position][new_damage].append((row, col))

    # 경로 추적
    results = deque([(N - 1, N - 1)])
    last_position = (N - 1, N - 1)
    while last_position:
        best_path = min(logs[last_position])
        last_position = logs[last_position][best_path][0]
        if last_position is None:
            break
        results.appendleft(last_position)

    # 결과 출력
    print(f'#{tc} {is_visited[N-1][N-1]}', ' '.join([f'{result[0]},{result[1]}' for result in results]))
