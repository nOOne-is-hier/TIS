import sys
import random

sys.stdin = open('input.txt')

# Input reading
N, M = map(int, input().split())

adjacency_list = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    adjacency_list[A - 1].append(B - 1)
    adjacency_list[B - 1].append(A - 1)

# Randomize the order of nodes for Floyd-Warshall
search_order = list(range(N))
random.shuffle(search_order)

# Initialize distances with a large value
distances = [[20000] * N for _ in range(N)]

# Set initial distances based on adjacency list
for row in range(N):
    distances[row][row] = 0
    for col in adjacency_list[row]:
        distances[row][col] = 1
        distances[col][row] = 1

# Apply Floyd-Warshall with randomized order to calculate shortest paths
for via in search_order:
    for start in search_order:
        for end in search_order:
            distances[start][end] = min(distances[start][end], distances[start][via] + distances[via][end])

# Step 2: Find the optimal pair of buildings to place chicken shops
min_total_distance = float('inf')
tmp_result = (float('inf'), 1, 2)

# Iterate over all combinations of two different buildings
for start in range(N):
    for end in range(start + 1, N):
        total_distance = 0
        for building in range(N):
            # Calculate the minimum distance to either of the two chicken shops
            distance_to_nearest_shop = min(distances[building][start], distances[building][end])
            # Since it's a round trip, multiply by 2
            total_distance += 2 * distance_to_nearest_shop

        # Update the optimal pair if a smaller total distance is found
        tmp_result = min((total_distance, start + 1, end + 1), tmp_result)

# Print the result
print(tmp_result[1], tmp_result[2], tmp_result[0])