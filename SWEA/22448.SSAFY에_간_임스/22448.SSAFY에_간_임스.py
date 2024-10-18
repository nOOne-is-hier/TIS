import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    result = [[] for _ in range(10)]
    for _ in range(N):
        problem, order = input().split()
        result[int(order) - 1].append(problem)
    print(f'#{tc}', end=' ')
    for line in result:
        if line:
            print(*sorted(line), end=' ')
    print()
