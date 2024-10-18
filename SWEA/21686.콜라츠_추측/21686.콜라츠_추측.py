def collatz_conjecture(N, counter=0):
    counter += 1
    if N % 2 == 0:
        N //= 2
        if N != 1:
            return collatz_conjecture(N, counter)
        return counter
    N *= 3
    N += 1
    if N != 1:
        return collatz_conjecture(N, counter)

    return counter

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc} {collatz_conjecture(int(input()))}')