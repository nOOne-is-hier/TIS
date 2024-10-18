import sys
sys.stdin = open('input.txt')

from collections import deque

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    beach = [list(input()) for _ in range(N)]

    last = deque()

    for r in range(N):
        for c in range(M):
            if beach[r][c] == 'L':
                last.append((r, c, 0))
            else:
                beach[r][c] = '0'

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while last:
        r, c, distance = last.popleft()
        if beach[r][c] == 'L':
            distance += 1
            around_num = []
            around_land = []
            around_ocean = False

            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]
                if 0 <= nr < N and 0 <= nc < M:

                    if beach[nr][nc] == '0':
                        beach[r][c] = distance
                        around_ocean = True
                        break

                    if type(beach[nr][nc]) != str:
                        around_num.append(beach[nr][nc])

                    else:
                        around_land.append((nr, nc, distance))

            if not around_ocean:
                if around_num:
                    beach[r][c] = min(around_num) + distance

                elif around_land:
                    for land in around_land:
                        last.append(land)
    print(beach)
    result = 0
    for r in range(N):
        for c in range(M):
            result += int(beach[r][c])

    print(f'#{tc} {result}')