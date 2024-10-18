import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    sums = []

    for start in range(N - M + 1):
        idx = 0 + start
        sum1 = 0
        for _ in range(M):
            sum1 += numbers[idx]
            idx += 1

        sums += [sum1]

    max_sum = sums[0]
    for num in sums:
        if num > max_sum:
            max_sum = num

    max_difference = max_sum - sums[0]
    for num in sums:
        if max_sum - num > max_difference:
            max_difference = max_sum - num

    print(f'#{tc}', max_difference)