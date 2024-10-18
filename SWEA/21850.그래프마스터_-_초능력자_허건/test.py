import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    was_zero = False

    teleport_count = 0
    if N == 0:
        was_zero = True
        N = 1

    if N < M:
        big = len(bin(M)) - 2
        small = len(bin(N)) - 2
        teleport_count += big - small

        # 정확하게 M에 도달하지 않은 경우 처리
        if N * 2**teleport_count != M:
            diff = M - N * 2**teleport_count
            if diff > 0:
                # 더 작은 2의 거듭제곱 수와 비교하여 최적의 경우 선택
                lower_bound = 2**(big-1)
                remaining_diff = M - lower_bound
                min_operations = min(bin(remaining_diff).count('1'), lower_bound - M + 2**big)
                teleport_count += min_operations
            else:
                teleport_count += bin(abs(diff)).count('1')

        if was_zero:
            teleport_count += 1

    elif M < N:
        teleport_count = N - M
        if was_zero:
            teleport_count -= 1

    else:
        if was_zero:
            teleport_count += 1

    print(f'#{tc} {teleport_count}')
