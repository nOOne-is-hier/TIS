import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = [0, 1, 3, 5]
    for i in range(4, N//10+1):
        result.append(result[i-2] * 3 + result[i-3] * 2)
    print(f'#{tc} {result[N//10]}')