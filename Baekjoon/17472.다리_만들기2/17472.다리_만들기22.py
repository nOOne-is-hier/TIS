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
                    borders = set()
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
                                else:
                                    is_border = True
                        if is_border:
                            borders.add((r, c))
                    islands.append(borders)


def find_edge(nodes):
    n = len(nodes)
    for start in range(n):
        for point in nodes[start]:
            to_right = point[1] + 1
            distance = (10, False)
            is_finish = False
            while to_right < M:
                if (point[0], to_right) in nodes[start]:
                    break
                if beach_map[point[0]][to_right]:
                    tmp_dis = abs(point[1] - to_right) - 1
                    if 2 <= tmp_dis < distance[0]:
                        for idx in range(n):
                            if (point[0], to_right) in nodes[idx]:
                                distance = (tmp_dis, idx)
                                is_finish = True
                                break
                    else:
                        break
                else:
                    to_right += 1
                if is_finish:
                    break
            if distance[1] is not False and distance[1] != start:
                adjacency_list[start].append(distance)
                adjacency_list[distance[1]].append((distance[0], start))

            to_below = point[0] + 1
            distance = (10, False)
            is_finish = False
            while to_below < N:
                if (to_below, point[1]) in nodes[start]:
                    break
                if beach_map[to_below][point[1]]:
                    tmp_dis = abs(point[0] - to_below) - 1
                    if 2 <= tmp_dis < distance[0]:
                        for idx in range(n):
                            if (to_below, point[1]) in nodes[idx]:
                                distance = (tmp_dis, idx)
                                is_finish = True
                                break
                    else:
                        is_finish = True
                else:
                    to_below += 1
                if is_finish:
                    break
            if distance[1] is not False:
                adjacency_list[start].append(distance)
                adjacency_list[distance[1]].append((distance[0], start))


def prim(adj):
    N = len(adj)
    is_visited = [0] * N
    order = [(0, 0)]
    total_cost = 0

    while order and sum(is_visited) < N:
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
adjacency_list = [[] for _ in range(len(islands))]
find_edge(islands)
print(adjacency_list)
print(prim(adjacency_list))