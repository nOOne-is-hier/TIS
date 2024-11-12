import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 델타 배열
dr = [0, 1]
dc = [1, 0]


def find_island(map, is_visited=None):
    if is_visited is None:
        is_visited = [[0] * M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if not is_visited[r][c]:
                is_visited[r][c] = 1
                if map[r][c]:
                    head = (N - 1, M - 1)
                    tail = (0, 0)
                    order = deque([(r, c)])
                    while order:
                        r, c = order.popleft()
                        head = min(head, (r, c))
                        tail = max(tail, (r, c))
                        for dir in range(2):
                            nr = r + dr[dir]
                            nc = c + dc[dir]
                            if 0 <= nr < N and 0 <= nc < M and map[nr][nc]:
                                is_visited[nr][nc] = 1
                                order.append((nr, nc))
                    islands.append((head, tail))


def find_edge(nodes):
    for start in len(nodes):
        for end in len(nodes):
            if nodes[start] == nodes[end]:
                continue
            if nodes[start][1][0] >= nodes[end][0][0] or nodes[start][0][0] <= nodes[end][1][0]:
                distance = min(abs(nodes[start][1][1] - nodes[end][0][1]), abs(nodes[start][0][1] - nodes[end][1][1]))
                if distance >= 2:
                    adjacency_list[start].append((end, distance))
            elif

N, M = map(int, input().split())
beach_map = [list(map(int, input().split())) for _ in range(N)]
islands = []
find_island(beach_map)
adjacency_list = [[] for _ in range(len(islands))]
print(islands)