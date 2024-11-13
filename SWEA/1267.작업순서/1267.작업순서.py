import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

for tc in range(1, 11):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    print(f'#{tc}', end=' ')

    adjacency_list = [[] for _ in range(V + 1)]
    in_degrees = [0] * (V + 1)
    for idx in range(E):
        pre, sub = edges[idx * 2], edges[idx * 2 + 1]
        adjacency_list[pre].append(sub)
        in_degrees[sub] += 1

    order = deque()
    for idx in range(1, V + 1):
        if in_degrees[idx] == 0:
            order.append(idx)
    result = deque()
    while order:
        cur_sub = order.popleft()
        result.append(cur_sub)
        for next_sub in adjacency_list[cur_sub]:
            in_degrees[next_sub] -= 1
            if in_degrees[next_sub] == 0:
                order.append(next_sub)

    print(*result)