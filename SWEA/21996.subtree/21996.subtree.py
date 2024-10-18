import sys
from collections import deque

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    tree_input = list(map(int, input().split()))

    adjacency_list = [[] for _ in range(N+2)]

    for idx in range(N):
        adjacency_list[tree_input[idx*2]].append(tree_input[(idx*2)+1])

    nodes = 0
    lasts = deque([E])

    while lasts:
        current = lasts.popleft()
        nodes += 1

        for child in adjacency_list[current]:
            lasts.append(child)

    print(f'#{tc} {nodes}')