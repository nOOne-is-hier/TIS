import sys

sys.stdin = open('input.txt')


def find(node):
    if node == parents[node]:
        return node

    return find(parents[node])


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    # if cycle return False
    if root_x == root_y:
        return False
    # 병합
    parents[root_y] = root_x
    return True


# 키워드: 같은 그룹끼리 union 연산이 발생하면 싸이클이 발생한다!

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    N = int(input())
    adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]

    # make-set
    parents = [idx for idx in range(N)]

    is_cycle = False
    for idx in range(N):
        for next_node in range(idx + 1, N): # 대각선 기준으로 우측 반만 확인
            if adjacency_matrix[idx][next_node] == 0:
                continue

            if not union(idx, next_node):                   # 두 노드를 연결, 두 노드가 같은 그룹이면 싸이클이 발생
                is_cycle = True
                break
        if is_cycle:
            print('WARNING')
            break
    if not is_cycle:
        print('STABLE')