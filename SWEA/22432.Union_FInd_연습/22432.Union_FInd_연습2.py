import sys

sys.stdin = open('input.txt')


def find(node):
    if node == parents[node]:
        return node

    parents[node] = find(parents[node])
    return parents[node]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return
    if root_x > root_y:
        parents[root_y] = root_x
    elif root_y > root_x:
        parents[root_x] = root_y


T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    N, Q = map(int, input().split())

    # make-set: 초기화 과정
    parents = [idx for idx in range(N + 1)]

    for _ in range(Q):
        K, A, B = map(int, input().split())
        if K == 0:
            if find(A) == find(B):
                print('YES', end=' ')
            else:
                print('NO', end=' ')
        if K == 1:
            union(A, B)
    print()