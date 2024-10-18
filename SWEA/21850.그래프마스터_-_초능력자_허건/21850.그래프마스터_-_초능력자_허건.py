import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, M = list(map(int, input().split()))

    teleport_count = 0
    while M != N:
        if M % 2 == 1:
            teleport_count += 1
            if M > N:
                M -= 1
            else:
                M += 1

        elif M % 2 == 0:
            if M > N and M//2 >= N:
                teleport_count += 1
                M //= 2
            elif M < N and M*2 <= N:
                teleport_count += 1
                M *= 2
            else:
                if M > N:
                    teleport_count += (M - N)
                    break
                elif M < N:
                    teleport_count += (N - M)
                    break

    print(f'#{tc} {teleport_count}')