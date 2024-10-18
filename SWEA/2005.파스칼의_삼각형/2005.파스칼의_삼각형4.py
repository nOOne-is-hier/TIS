import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    start = 1
    lines = []
    while start <= N:
        if start <= 2:
            line = []
            for _ in range(start):
                line += [1]
            lines += [line]
            print(*line)
            start += 1

        else:
            line = [0] * start
            for idx in range(start-1):
                last = lines[start-2].pop()
                line[idx] += last
                line[idx+1] = last
            lines += [line]
            print(*line)
            start += 1