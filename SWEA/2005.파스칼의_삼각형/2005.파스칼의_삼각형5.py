import sys
sys.stdin = open('input.txt')

def pascal_trianlge(N):
    if N <= 0:
        return []

    triangle = [[1]]

    for i in range(1, N):
        line = [1]
        for j in range(1, i):
            line.append(triangle[i-1][j-1] + triangle[i-1][j])
        line.append(1)
        triangle.append(line)

    return triangle

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())
    triangle = pascal_trianlge(N)

    for line in triangle:
        print(*line)