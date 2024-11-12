import sys
from collections import deque
from heapq import heappop, heappush
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 델타 배열
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def find_island(map):
    is_visited = [[0] * M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if not is_visited[r][c]:
                is_visited[r][c] = 1
                if map[r][c]:
                    borders = []
                    order = deque([(r, c)])
                    while order:
                        r, c = order.popleft()
                        is_border = False
                        for dir in range(4):
                            nr = r + dr[dir]
                            nc = c + dc[dir]
                            if 0 <= nr < N and 0 <= nc < M:
                                if map[nr][nc]:
                                    if not is_visited[nr][nc]:
                                        is_visited[nr][nc] = 1
                                        order.append((nr, nc))
                                elif not map[nr][nc]:
                                    is_border = True
                        if is_border:
                            borders.append((r, c))
                    islands.append(borders)


def find_edge(nodes):
    N = len(nodes)
    for start in range(N):
        for end in range(N):
            if start == end:
                continue
            distance = 10
            tmp_dis = 0
            for border1 in nodes[start]:
                for border2 in nodes[end]:
                    if border1[0] == border2[0]:
                        tmp_dis = abs(border1[1] - border2[1]) - 1
                    elif border1[1] == border2[1]:
                        tmp_dis = abs(border1[0] - border2[0]) - 1
                    if 0 < tmp_dis:
                        distance = min(distance, tmp_dis)
            if 2 <= distance < 10:
                adjacency_list[start].append((distance, end))


def prim(adj):
    N = len(adj)
    is_visited = [0] * N
    order = [(0, 0)]
    total_cost = 0

    while order:
        weight, node = heappop(order)
        if is_visited[node]:
            continue
        is_visited[node] = 1
        total_cost += weight

        for w_v in adj[node]:
            if not is_visited[w_v[1]]:
                heappush(order, w_v)

    if sum(is_visited) < N:
        return -1

    return total_cost


N, M = map(int, input().split())
beach_map = [list(map(int, input().split())) for _ in range(N)]
islands = []
find_island(beach_map)
print(islands)
adjacency_list = [[] for _ in range(len(islands))]
find_edge(islands)
print(adjacency_list)
print(prim(adjacency_list))