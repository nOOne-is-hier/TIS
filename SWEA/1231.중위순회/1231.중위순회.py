import sys
sys.stdin = open('input.txt')

from collections import deque

for tc in range(1, 11):
    print(f'#{tc}', end=' ')
    N = int(input())
    array_tree = [0] * (N + 1)
    for _ in range(1, N + 1):
        idx, char, *children = input().split()
        array_tree[int(idx)] = char

    current = 1
    stack = deque()

    while stack or current <= N:

        if current <= N:
            stack.append(current)
            current *= 2
            continue

        else:
            current = stack.pop()
            print(array_tree[current], end='')
            current = current * 2 + 1

    print()
