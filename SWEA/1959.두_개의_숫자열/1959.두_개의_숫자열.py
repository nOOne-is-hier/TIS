import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    length_A, length_B = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_sum = 0

    # 두 배열의 길이가 다르다면
    if length_A != length_B:

        if length_A > length_B:
            long = A
            short = B

        elif length_A < length_B:
            long = B
            short = A

        for difference in range(abs(length_A-length_B)+1):
            total = 0
            for idx in range(len(short)):
                total += short[idx] * long[idx+difference]
            if max_sum < total:
                max_sum = total

        print(max_sum)

    # 두 배열의 길이가 같다면
    else:
        total = 0
        for idx in range(length_A):
            total += A[idx] * B[idx]

        print(total)