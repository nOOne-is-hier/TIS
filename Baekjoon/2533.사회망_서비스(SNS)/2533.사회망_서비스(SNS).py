import sys
from collections import deque
sys.stdin = open('input.txt')


def DFS(node=0, last=-1):
    for child in adjacency_list[node]:
        if child != last:
            parents[child] = node
            DFS(child, node)


N = int(input())

adjacency_list = [[] for _ in range(N)]
parents = [-1] * N

for _ in range(N - 1):
    parent, child = map(int, input().split())
    adjacency_list[parent - 1].append(child - 1)
    adjacency_list[child - 1].append(parent - 1)
    print(adjacency_list)

root_node = parents.index(-1)
order = deque([(root_node, -1)])
odd_level = 0
even_level = 0
is_odd = True

while order:
    in_this_level = len(order)
    next_order = deque()

    for _ in range(in_this_level):
        current, last = order.popleft()

        for child in adjacency_list[current]:
            if child != last:
                next_order.append((child, current))

    if is_odd:
        odd_level += in_this_level
    else:
        even_level += in_this_level

    is_odd = not is_odd
    order.extend(next_order)
print(odd_level, even_level)
if min(odd_level, even_level):
    print(min(odd_level, even_level))
else:
    print(max(odd_level, even_level))