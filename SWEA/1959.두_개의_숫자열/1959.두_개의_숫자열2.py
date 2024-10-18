import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    length_A, length_B = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_sum = 0

    if length_A >= length_B:
        for idx in range(length_A-length_B+1):
            total = 0
            for num in range(length_B):
                total += B[num] * A[idx+num]

            if max_sum < total:
                max_sum = total

    else:
        for idx in range(length_B - length_A + 1):
            total = 0
            for num in range(length_A):
                total += A[num] * B[idx + num]

            if max_sum < total:
                max_sum = total

    print(max_sum)