import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())

    cables = [list(map(int, input().split())) for _ in range(N)]

    intersections = 0
    for reference in range(N - 1):
        for comparison in range(reference + 1, N):
            if cables[reference][0] < cables[comparison][0] and cables[reference][1] > cables[comparison][1]:
                intersections += 1
            elif cables[reference][0] > cables[comparison][0] and cables[reference][1] < cables[comparison][1]:
                intersections += 1

    print(f'#{tc} {intersections}')