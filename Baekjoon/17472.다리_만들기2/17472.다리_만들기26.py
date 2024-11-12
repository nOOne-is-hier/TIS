from collections import deque
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

# Find and label islands using BFS
def find_islands(grid, n, m):
    island_id = 2
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    islands = {}

    def bfs(x, y):
        queue = deque([(x, y)])
        grid[x][y] = island_id
        island = [(x, y)]

        while queue:
            cx, cy = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    grid[nx][ny] = island_id
                    queue.append((nx, ny))
                    island.append((nx, ny))
        return island

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                islands[island_id] = bfs(i, j)
                island_id += 1

    return islands

# Build bridge connections between islands with BFS for minimal distances
def build_bridges(grid, islands, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    edges = []

    for island_id, positions in islands.items():
        for x, y in positions:
            for dx, dy in directions:
                length = 0
                nx, ny = x + dx, y + dy
                while 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == island_id:
                        break
                    if grid[nx][ny] > 1:
                        if length > 1:
                            edges.append((length, island_id, grid[nx][ny]))
                        break
                    nx += dx
                    ny += dy
                    length += 1

    return edges

# Union-Find functions for Kruskal's algorithm
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, rank, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            rank[root_a] += 1

# Optimized minimum bridge length calculation
def minimum_bridge_length(n, m, grid):
    islands = find_islands(grid, n, m)
    edges = build_bridges(grid, islands, n, m)

    edges.sort()  # Sort edges by length
    parent = {i: i for i in islands.keys()}
    rank = {i: 0 for i in islands.keys()}

    total_length = 0
    connected_edges = 0

    # Kruskal's algorithm to find MST
    for length, island_a, island_b in edges:
        if find_parent(parent, island_a) != find_parent(parent, island_b):
            union_parent(parent, rank, island_a, island_b)
            total_length += length
            connected_edges += 1
            if connected_edges == len(islands) - 1:
                return total_length

    return -1

# 입력 처리
N, M = map(int, input().split())
beach_map = [list(map(int, input().split())) for _ in range(N)]

# Output
print(minimum_bridge_length(N, M, beach_map))

