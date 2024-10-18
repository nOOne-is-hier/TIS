import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pollens = [list(map(int, input().split())) for _ in range(N)]
    # 델타 좌표
    dr = [0, 0, 1, 0, -1]
    dc = [0, 1, 0, -1, 0]

    pollen_sums = []
    for row in range(N):
        for column in range(M):
            pollen_sum = 0
            for idx in range(5):
                if 0 <= row+dr[idx] < N and 0 <= column+dc[idx] < M:
                    pollen_sum += pollens[row+dr[idx]][column+dc[idx]]
            pollen_sums += [pollen_sum]

    max_sum = pollen_sums[0]
    for s in pollen_sums:
        if max_sum < s:
            max_sum = s

    print(f'#{tc}', max_sum)