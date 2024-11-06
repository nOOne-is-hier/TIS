import sys

sys.stdin = open('input.txt')


class MaxNum(int):
    def __str__(self):
        return '-1'


def is_united(nodes):
    is_visited = 0
    start_node = nodes & -nodes


    def dfs(node_mask):
        nonlocal is_visited
        is_visited |= node_mask
        neighbors = adjacency_list[node_mask.bit_length() - 1]
        for neighbors_mask in (1 << i for i in range(N) if (neighbors & (1 << i)) and (nodes & (1 << i ))):
            if not is_visited & neighbors_mask:
                dfs(neighbors_mask)


    dfs(start_node)

    return is_visited == nodes


N = int(input())
peoples = list(map(int, input().split()))
adjacency_list = [0] * N
for idx in range(N):
    _, *nodes = map(int, input().split())
    for i in nodes:
        adjacency_list[idx] |= 1 << i - 1

total = sum(peoples)
min_dif = MaxNum(1001)
for case in range(1, 2 ** (N - 1)):
    district1 = case
    group1_popularity = sum(peoples[idx] for idx in range(N) if district1 & (1 << idx))
    diff = abs(total - (group1_popularity << 1))
    if diff >= min_dif:
        continue

    district2 = ((1 << N) - 1) ^ case
    if is_united(district1) and is_united(district2):
        min_dif = min(min_dif, diff)

print(min_dif)
