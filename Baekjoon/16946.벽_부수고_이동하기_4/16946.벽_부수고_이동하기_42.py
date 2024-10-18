import sys
from collections import deque
sys.stdin = open('input.txt')


def BFS(idx):
    # 델타 배열
    d = [-M, 1, M, -1]

    cells_to_move = 1
    order = deque([idx])
    map_info[idx] = -1
    indices = set()

    while order:
        i = order.popleft()

        for dir in range(4):
            ni = i + d[dir]

            if (dir % 2 == 0 and 0 <= ni < N * M) or (dir % 2 == 1 and i // M == ni // M):
                if map_info[ni] == '0':
                    order.append(ni)
                    map_info[ni] = -1
                    cells_to_move += 1
                elif map_info[ni] == '1':
                    indices.add(ni)

    for idx in indices:
        is_visited[idx] = int(is_visited[idx]) + cells_to_move


N, M = map(int, input().split())
map_info = []
for _ in range(N):
    map_info.extend(list(input().strip()))
is_visited = map_info[:]

for idx in range(N * M):
    if is_visited[idx] == '0' and map_info[idx] != -1:
        BFS(idx)

for idx in range(N * M):
    if is_visited[idx] != '0':
        is_visited[idx] = str(int(is_visited[idx]) % 10)

left = 0
right = M
while right <= N * M:
    print(''.join(is_visited[left:right]))
    left, right = left + M, right + M
