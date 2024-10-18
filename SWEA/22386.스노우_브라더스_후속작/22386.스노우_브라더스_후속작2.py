import heapq
import sys

sys.stdin = open('input.txt')

# 델타 배열
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    snowBrothers = [list(map(int, input().split())) for _ in range(N)]

    # 시작과 도착점을 탐색
    start_point = end_point = 0
    for r, c in ((r, c) for r in range(N) for c in range(M)):
        if snowBrothers[r][c] == 2:
            start_point = (r, c)
        elif snowBrothers[r][c] == 3:
            end_point = (r, c)
        if start_point and end_point:
            break

    # 다익스트라를 이용한 비용 탐색
    is_visited = [[0] * M for _ in range(N)]
    orders = [(0, 0, start_point)]

    while orders:
        min_cost, current_cost, (r, c) = heapq.heappop(orders)

        # 방문 처리
        is_visited[r][c] = 1

        # 기저 조건
        if (r, c) == end_point:
            print(f'#{tc}', min_cost)
            break

        for dir in range(4):
            nr = r + direction[dir][0]; nc = c + direction[dir][1]
            if 0 <= nr < N and 0 <= nc < M and not is_visited[nr][nc]:
                # 좌우 이동
                if dir < 2:
                    if snowBrothers[r][c] and snowBrothers[nr][nc]:
                        heapq.heappush(orders, (min_cost, current_cost, (nr, nc)))
                # 상하 이동
                else:
                    new_cost = max(min_cost, current_cost + 1)
                    if not snowBrothers[nr][nc]:
                        heapq.heappush(orders, (new_cost, current_cost + 1, (nr, nc)))
                    else:
                        heapq.heappush(orders, (new_cost, 0, (nr, nc)))