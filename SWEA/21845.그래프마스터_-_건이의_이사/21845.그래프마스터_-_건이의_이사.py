import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, M = list(map(int, input().split()))
    lines = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end = list(map(int, input().split()))
        lines[start] += [end]
        lines[end] += [start]
    R, K = list(map(int, input().split()))

    candidates = set()
    distance = 0
    stack = [lines[R]]
    candidates.add(R)

    while distance != K:
        distance += 1
        for _ in range(len(stack)):
            current = stack.pop(0)

            for vertex in current:
                stack.append(lines[vertex])
                candidates.add(vertex)

    print(f'#{tc} {len(candidates)}')