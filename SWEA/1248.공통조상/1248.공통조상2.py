import sys
from collections import deque

sys.stdin = open('input.txt')


def find_root(node, parents=None):

    if parents is None:
        parents = deque()

    parents.append(node)

    if not inverse_list[node]:
        return parents

    for parent in inverse_list[node]:
        return find_root(parent, parents)


T = int(input())

for tc in range(1, T + 1):
    V, E, N1, N2 = map(int, input().split())
    N1 -= 1; N2 -= 1
    adjacency_list = [[] for _ in range(V)]
    inverse_list = [[] for _ in range(V)]
    edges = list(map(int, input().split()))
    for idx in range(E):
        parent = edges[idx * 2]
        child = edges[idx * 2 + 1]
        adjacency_list[parent - 1].append(child - 1)
        inverse_list[child - 1].append(parent - 1)
    parent1 = find_root(N1)
    parent2 = find_root(N2)

    common_parent = next((node1 for node1 in parent1 for node2 in parent2 if node1 == node2), None)

    subtree_size = 1
    order = deque([common_parent])
    while order:
        current = order.popleft()
        for child in adjacency_list[current]:
            subtree_size += 1
            order.append(child)

    print(f'#{tc}', common_parent + 1, subtree_size)
