import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    former_lines = []
    print(f'#{tc}')
    for num in range(1, N + 1):
        line = [1] * num
        if num > 2:
            for n in range(1, num - 1):
                line[n] = former_lines[num-2][n-1] + former_lines[num-2][n]
        print(*line)
        former_lines += [line]