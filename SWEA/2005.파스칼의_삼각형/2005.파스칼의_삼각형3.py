import sys
sys.stdin = open('input.txt')

def pascal_triangle(number, memo={1: [1], 2: [1, 1]}):
    if number < 3:
        return memo
    else:
        line = [1] * number
        for num in range(1, number-1):
            line[num] = memo[number-1][num-1] + memo[number-1][num]
        memo[number] = line
        return pascal_triangle(number-1, memo)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    result = pascal_triangle(N)
    for num in range(1, N+1):
        print(*result[num])


