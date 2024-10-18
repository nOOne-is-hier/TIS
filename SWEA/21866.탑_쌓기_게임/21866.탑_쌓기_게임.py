import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M1, M2 = list(map(int, input().split()))
    blocks = sorted(list(map(int, input().split())))

    total_cost = 0
    difference = abs(M1-M2)
    upper_level = reversed(blocks[:difference])
    same_level = reversed(blocks[difference:])

    idx = 2
    for num in same_level:
        total_cost += num * int(idx/2)
        start = int(idx/2) + 1
        idx += 1

    for num in upper_level:
        total_cost += num * start
        start += 1

    print(f'#{tc} {total_cost}')