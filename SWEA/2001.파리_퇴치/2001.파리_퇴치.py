import sys

sys.stdin = open('input.txt')

T = int(input())


def coordinate_grid_sum(x, y, side, lst):
    dx = dy = -1
    total = 0
    for _ in range(side):
        dy = -1
        dx += 1
        for _ in range(side):
            dy += 1
            total += lst[x+dx][y+dy]

    return total


for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    flies = [list(map(int, input().split())) for _ in range(N)]
    flies_death = []
    for r in range(N-M+1):
        for c in range(N-M+1):
            flies_death += [coordinate_grid_sum(r, c, M, flies)]

    print(f'#{tc}', max(flies_death))
