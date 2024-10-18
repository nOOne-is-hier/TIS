import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())

    array = [0] * (N + 1)

    for _ in range(M):
        idx, num = map(int, input().split())
        array[idx] = num

    for idx in range(N, 0, -1):
        array[idx//2] += array[idx]

    print(f'#{tc} {array[L]}')