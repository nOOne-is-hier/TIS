import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    N = int(input())
    if bin(N)[-1] != '1':
        print('YES')
    else:
        print('NO')
