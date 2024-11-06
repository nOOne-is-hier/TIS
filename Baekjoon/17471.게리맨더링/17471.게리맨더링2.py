import sys

sys.stdin = open('input.txt')


class MaxNum(float):

    def __str__(self):
        return '-1'


def is_united(nodes):
    is_visited = set()
    start_node = next(iter(nodes))


    def dfs(node):
        is_visited.add(node)
        for neighbor in adjacency_list[node]:
            if neighbor in nodes and neighbor not in is_visited:
                dfs(neighbor)


    dfs(start_node)

    return is_visited == nodes


N = int(input())
peoples = list(map(int, input().split()))
adjacency_list = [-1] * N
for idx in range(N):
    _, *nodes = map(int, input().split())
    for i in range(len(nodes)):
        nodes[i] -= 1
    adjacency_list[idx] = nodes

min_dif = MaxNum('inf')
for case in range(1, 2 ** N // 2):
    district1 = set()
    district2 = set()
    for idx in range(N):
        if case & (1 << idx):
            district1.add(idx)
        else:
            district2.add(idx)
    if is_united(district1):
        if is_united(district2):
            people1 = sum(peoples[district] for district in district1)
            people2 = sum(peoples[district] for district in district2)
            min_dif = min(min_dif, abs(people1 - people2))

print(min_dif)

