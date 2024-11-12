import sys
from collections import deque
from heapq import heappop, heappush

sys.stdin = open('input.txt')
input = sys.stdin.readline

# 델타 배열
dr = [0, 1, 0, -1]  # 동, 남, 서, 북
dc = [1, 0, -1, 0]


def find_island(beach_map):
    is_visited = [[0] * M for _ in range(N)]
    island_count = 0  # 섬 번호 매핑용
    islands = []

    for r in range(N):
        for c in range(M):
            if beach_map[r][c] == 1 and not is_visited[r][c]:
                island_count += 1
                queue = deque([(r, c)])
                is_visited[r][c] = island_count
                current_island = []

                while queue:
                    cr, cc = queue.popleft()
                    current_island.append((cr, cc))

                    for dir in range(4):
                        nr, nc = cr + dr[dir], cc + dc[dir]
                        if 0 <= nr < N and 0 <= nc < M and not is_visited[nr][nc]:
                            if beach_map[nr][nc] == 1:
                                is_visited[nr][nc] = island_count
                                queue.append((nr, nc))

                islands.append(current_island)

    return islands, is_visited


def find_edge(islands, is_visited):
    adjacency_list = [[] for _ in range(len(islands))]

    for island_num, island in enumerate(islands, start=1):
        for (r, c) in island:
            # 네 방향으로 최소 거리 탐색
            for dir in range(4):
                distance = 0
                nr, nc = r + dr[dir], c + dc[dir]

                while 0 <= nr < N and 0 <= nc < M:
                    if is_visited[nr][nc] == island_num:
                        break  # 같은 섬 내에서는 다리를 놓을 필요가 없음
                    elif is_visited[nr][nc] > 0:
                        if distance >= 2:  # 거리가 2 이상인 경우만 유효한 간선으로 고려
                            target_island_num = is_visited[nr][nc] - 1
                            adjacency_list[island_num - 1].append((distance, target_island_num))
                            adjacency_list[target_island_num].append((distance, island_num - 1))
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


# 입력 처리
N, M = map(int, input().split())
beach_map = [list(map(int, input().split())) for _ in range(N)]

# 섬과 방문 배열 찾기
islands, is_visited = find_island(beach_map)

# 간선 목록 생성
adjacency_list = find_edge(islands, is_visited)

# 프림 알고리즘을 통한 최소 신장 트리 비용 계산
print(prim(adjacency_list))
