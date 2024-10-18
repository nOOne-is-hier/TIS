import sys
from collections import deque

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    beach = [0] * N
    last = deque()

    for r in range(N):
        line = input()
        row = [0] * M
        c = 0
        for char in line:
            if char == 'W':
                last.append((r, c, 0))
            elif char == 'L':
                row[c] = -1
            c += 1
        beach[r] = row

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while last:
        r, c, distance = last.popleft()

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0 <= nr < N and 0 <= nc < M and beach[nr][nc] == -1:  # 'L'은 -1로 변환됨
                beach[nr][nc] = distance + 1
                last.append((nr, nc, distance + 1))

    result = sum(map(sum, beach))
    print(f'#{tc} {result}')
