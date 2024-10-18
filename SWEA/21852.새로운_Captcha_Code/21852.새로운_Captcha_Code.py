import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    N, K = list(map(int, input().split()))
    Sample = input().split()
    PassCode = input().split()

    idx = 0
    for num in Sample:
        if idx == K:
            print(1)
            break
        if num == PassCode[idx]:
            idx += 1

    else:
        print(0)
