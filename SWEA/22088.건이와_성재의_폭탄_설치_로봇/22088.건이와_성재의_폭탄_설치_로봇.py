import sys
sys.stdin = open('input.txt')

import heapq

for tc in range(1, int(input()) + 1):
    test_field = [[0] * 1000 for _ in range(1000)]
    N, M = map(int, input().split())

    orders = []

    # 델타 배열
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for _ in range(N + M):
        is_exploded = False
        order = list(map(int, input().split()))
        if order[0]:
            heapq.heappush(orders, order)

        else:
            while not is_exploded and orders:
                num, row, column = heapq.heappop(orders)
                if not test_field[row][column]:
                    test_field[row][column] = 1
                    print(f'#{tc} {num}')
                    for dir in range(4):
                        nr = row + dr[dir]
                        nc = column + dc[dir]
                        if 0 <= nr < 1000 and 0 <= nc < 1000:
                            test_field[nr][nc] = 1
                    is_exploded = True

        if not is_exploded and not orders:
            print(f'#{tc} -1')