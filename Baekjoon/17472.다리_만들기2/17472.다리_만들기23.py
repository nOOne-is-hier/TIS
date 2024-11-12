import sys
from collections import deque
from heapq import heappop, heappush

sys.stdin = open('input.txt')
input = sys.stdin.readline

# 델타 배열
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def find_island(beach_map):
    is_visited = [[0] * M for _ in range(N)]
    islands = []

    for r in range(N):
        for c in range(M):
            if not is_visited[r][c] and beach_map[r][c] == 1:
                borders = set()
                queue = deque([(r, c)])
                is_visited[r][c] = 1

                while queue:
                    cr, cc = queue.popleft()
                    is_border = False

                    for dir in range(4):
                        nr, nc = cr + dr[dir], cc + dc[dir]
                        if 0 <= nr < N and 0 <= nc < M:
                            if beach_map[nr][nc] == 1 and not is_visited[nr][nc]:
                                is_visited[nr][nc] = 1
                                queue.append((nr, nc))
                            elif beach_map[nr][nc] == 0:
                                is_border = True

                    if is_border:
                        borders.add((cr, cc))

                islands.append(borders)
    return islands

def find_edge(islands):
    adjacency_list = [[] for _ in range(len(islands))]

    for start, island in enumerate(islands):
        for (r, c) in island:
            for dir in range(2):  # 오른쪽과 아래쪽만 탐색
                distance = 0
                nr, nc = r + dr[dir], c + dc[dir]

                while 0 <= nr < N and 0 <= nc < M:
                    if (nr, nc) in island:
                        break
                    if beach_map[nr][nc] == 1:
                        for end, target_island in enumerate(islands):
                            if (nr, nc) in target_island and start != end:
                                if distance >= 2:
                                    adjacency_list[start].append((distance, end))
                                    adjacency_list[end].append((distance, start))
                                break
                        break

                    nr += dr[dir]
                    nc += dc[dir]
                    distance += 1
    return adjacency_list

def prim(adj):
    total_cost = 0
    is_visited = [False] * len(adj)
    min_heap = [(0, 0)]
    num_visited = 0

    while min_heap and num_visited < len(adj):
        weight, node = heappop(min_heap)
        if is_visited[node]:
            continue

        is_visited[node] = True
        total_cost += weight
        num_visited += 1

        for edge_weight, neighbor in adj[node]:
            if not is_visited[neighbor]:
                heappush(min_heap, (edge_weight, neighbor))

    if num_visited == len(adj):
        return total_cost
    else:
        return -1

N, M = map(int, input().split())
beach_map = [list(map(int, input().split())) for _ in range(N)]

islands = find_island(beach_map)
adjacency_list = find_edge(islands)

print(prim(adjacency_list))
