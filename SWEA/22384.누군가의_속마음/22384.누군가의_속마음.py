import sys
sys.stdin = open('input.txt')
import heapq

# 델타 배열
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

T = int(input())

for tc in range(1, T + 1):
    start_r, start_c = map(int, input().split())
    N = int(input())
    map_of_town = [list(map(int, input().split())) for _ in range(N)]
    # 최소값 추적 배열
    min_fatigue = [[float('inf')] * N for _ in range(N)]
    orders = [(map_of_town[start_r][start_c], start_r, start_c)]

    # 다익스트라 시작
    while orders:
        current_fatigue, y, x = heapq.heappop(orders)

        # 피로도 비교 후 prunning
        if current_fatigue > min_fatigue[y][x]:
            continue

        # 4방위 탐색
        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            # 경계 설정
            if 0 <= ny < N and 0 <= nx < N and map_of_town[ny][nx] != -1:
                next_fatigue = current_fatigue + map_of_town[ny][nx]

                # 피로도를 갱신할 수 있는가?
                if min_fatigue[ny][nx] > next_fatigue:
                    min_fatigue[ny][nx] = next_fatigue
                    heapq.heappush(orders, (next_fatigue, ny, nx))

    # 결과 값 탐색
    max_fatigue = max(min_fatigue[r][c] for r in range(N) for c in range(N) if map_of_town[r][c] != -1)
    print(f'#{tc}', max_fatigue)