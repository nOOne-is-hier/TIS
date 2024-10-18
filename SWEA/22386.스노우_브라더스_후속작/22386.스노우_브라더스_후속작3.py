from heapq import heappush, heappop
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
    cost_table = [[21e9] * M for _ in range(N)]
    orders = [(0, start_point)]
    cost_table[start_point[0]][start_point[1]] = 0  # 시작점의 비용은 0

    while orders:
        current_cost, (r, c) = heappop(orders)

        # base condition
        if (r, c) == end_point:
            print(f'#{tc}', current_cost)
            break

        for dir in range(4):
            nr = r + direction[dir][0]
            nc = c + direction[dir][1]

            if 0 <= nr < N and 0 <= nc < M:
                if dir < 2:
                    if snowBrothers[nr][nc] and cost_table[nr][nc] > current_cost:
                        cost_table[nr][nc] = current_cost
                        heappush(orders, (current_cost, (nr, nc)))

                else:
                    height = 1
                    while 0 <= nr < N:
                        if not snowBrothers[nr][nc]:
                            height += 1
                            nr += direction[dir][0]
                            continue
                        new_cost = max(height, current_cost)
                        if cost_table[nr][nc] > new_cost:
                            cost_table[nr][nc] = new_cost
                            heappush(orders, (new_cost, (nr, nc)))
                        break