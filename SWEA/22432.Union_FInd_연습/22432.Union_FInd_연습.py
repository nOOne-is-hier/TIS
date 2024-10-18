import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    N, Q = map(int, input().split())
    table = [0] * (N + 1)
    for idx in range(1, N + 1):
        table[idx] =  idx
    for _ in range(Q):
        K, A, B = map(int, input().split())

        if K == 1:
            if table[A] != table[B]:
                representative = max(table[A], table[B])
                will_change = min(table[A], table[B])
                for idx in range(1, N + 1):
                    if table[idx] == table[will_change]:
                        table[idx] = table[representative]
                continue

        elif K == 0:
            if table[A] == table[B]:
                print('YES', end=' ')
            else:
                print('NO', end=' ')
    print()