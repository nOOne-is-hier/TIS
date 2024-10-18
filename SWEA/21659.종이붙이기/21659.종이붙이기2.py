import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(int(input())/10)
    sums = [1]
    for idx in range(1, N):
        if idx % 2 == 1:
            sums.append(sums[idx-1]*2+1)
        else:
            sums.append(sums[idx-1]*2-1)

    print(f'#{tc} {sums[-1]}')