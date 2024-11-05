import sys
from collections import deque

sys.stdin = open('input.txt')


def DFS(v1, v2, node=0, is_met1=None, is_met2=None):
    if is_met1 is None:
        is_met1 = [False]

    if is_met2 is None:
        is_met2 = [False]

    # subtree_size = 1

    if not adjacency_list[node][0]:
        # return subtree_size
        return 1

    if not is_met1[0]:
        parent1.appendleft(node)
    if not is_met2[0]:
        parent2.appendleft(node)

    for child in adjacency_list[node][0]:
        if child == v1:
            parent1.appendleft(child)
            is_met1[0] = True
        if child == v2:
            parent2.appendleft(child)
            is_met2[0] = True
        adjacency_list[node][1] += DFS(v1, v2, child, is_met1, is_met2)

    # adjacency_list[node][1] = subtree_size

    if not is_met1[0]:
        parent1.popleft()
    if not is_met2[0]:
        parent2.popleft()

    return adjacency_list[node][1]


T = int(input())

for tc in range(1, T + 1):
    V, E, N1, N2 = map(int, input().split())
    N1 -= 1; N2 -= 1
    adjacency_list = [[[], 1] for _ in range(V)]
    edges = list(map(int, input().split()))
    for idx in range(E):
        parent = edges[idx * 2]
        child = edges[idx * 2 + 1]
        adjacency_list[parent - 1][0].append(child - 1)
    parent1 = deque()
    parent2 = deque()

    DFS(N1, N2)
    common_parent = next((node1 for node1 in parent1 for node2 in parent2 if node1 == node2), None)
    print(f'#{tc}', common_parent + 1, adjacency_list[common_parent][1])
