import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    subsets_N =[]

    for num in range(2**12):
        subset = []
        for idx in range(12):
            if num & (1 << idx):
                subset += [numbers[idx]]

        if len(subset) == N:
            subsets_N += [subset]

    case_same_sum = 0
    for subset in subsets_N:
        if sum(subset) == K:
            case_same_sum += 1

    print(f'#{tc}', case_same_sum)