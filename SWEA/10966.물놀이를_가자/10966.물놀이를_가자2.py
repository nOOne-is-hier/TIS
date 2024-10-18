import sys
sys.stdin = open('input.txt')

from collections import deque

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    beach = [list(input()) for _ in range(N)]

    last = deque()

    for r in range(N):
        for c in range(M):
            if beach[r][c] == 'W':
                last.append((r, c, 0))
                beach[r][c] = 0

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while last:
        r, c, distance = last.popleft()

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0 <= nr < N and 0 <= nc < M and beach[nr][nc] == 'L':
                beach[nr][nc] = distance + 1
                last.append((nr, nc, distance + 1))
                # for line in beach:
                #     print(*line)
                # print()

                # else:
                #     beach[nr][nc] = min(beach[nr][nc], distance + 1)
                #     for line in beach:
                #         print(*line)
                #     print()

    # for line in beach:
    #     print(*line)
    result = sum(map(sum, beach))

    print(f'#{tc} {result}')