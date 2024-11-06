import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    V, E, N1, N2 = map(int, input().split())
    N1 -= 1;
    N2 -= 1
    adjacency_list = [[] for _ in range(V)]
    inverse_list = [[] for _ in range(V)]
    edges = list(map(int, input().split()))
    for idx in range(E):
        parent = edges[idx * 2]
        child = edges[idx * 2 + 1]
        adjacency_list[parent - 1].append(child - 1)
        inverse_list[child - 1].append(parent - 1)

    common_parent = 0
    parents1 = set()
    parents2 = set()
    order1 = deque([N1])
    order2 = deque([N2])
    while order1 or order2:
        if order1:
            current1 = order1.popleft()
        if order2:
            current2 = order2.popleft()

        parents1.add(current1)
        parents2.add(current2)

        if current1 in parents2:
            common_parent = current1
            break

        if current2 in parents1:
            common_parent = current2
            break

        for parent in inverse_list[current1]:
            order1.append(parent)

        for parent in inverse_list[current2]:
            order2.append(parent)

    subtree_size = 1
    order = deque([common_parent])
    while order:
        current = order.popleft()
        for child in adjacency_list[current]:
            subtree_size += 1
            order.append(child)

    print(f'#{tc}', common_parent + 1, subtree_size)
