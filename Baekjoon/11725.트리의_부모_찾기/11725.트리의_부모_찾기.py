import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(input())

adjacency_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    start, end = map(int, input().split())
    adjacency_list[start] += [end]
    adjacency_list[end] += [start]

inverse_oneway_list = [0] * (N + 1)
last = deque([1])
is_visited = [0] * (N + 1)

while last:
    current = last.popleft()
    if is_visited[current]:
        continue
    is_visited[current] = 1

    for node in adjacency_list[current]:
        if not is_visited[node]:
            inverse_oneway_list[node] = current
            last.append(node)

for idx in range(2, N + 1):
    print(inverse_oneway_list[idx])