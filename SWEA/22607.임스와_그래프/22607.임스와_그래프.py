import heapq
import sys
from collections import defaultdict

def dijkstra(start, graph):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def solve(test_cases):
    results = []
    for t in range(len(test_cases)):
        n, edges = test_cases[t]
        graph = defaultdict(dict)

        # Build the graph
        for x, y, cost in edges:
            graph[x][y] = cost
            graph[y][x] = cost

        # Run Dijkstra from 'a' and 'Z' (ensure both nodes are in the graph)
        if 'a' in graph and 'Z' in graph:
            ims_distances = dijkstra('a', graph)
            banssafi_distances = dijkstra('Z', graph)
        else:
            results.append(f"#{t + 1} NO")
            continue

        # Compare the distances from 'a' to 'Z' and 'Z' to 'a'
        ims_cost = ims_distances.get('Z', float('inf'))
        banssafi_cost = banssafi_distances.get('a', float('inf'))

        if ims_cost == float('inf') or banssafi_cost == float('inf'):
            results.append(f"#{t + 1} NO")
        elif ims_cost <= banssafi_cost:
            results.append(f"#{t + 1} YES {ims_cost}")
        else:
            results.append(f"#{t + 1} NO")

    return results

def main():
    sys.stdin = open('input.txt')
    idx = 0
    T = int(input())
    idx += 1

    test_cases = []
    for _ in range(T):
        N = int(input())
        idx += 1
        edges = []
        for _ in range(N):
            start, end, cost = input().split()
            cost = int(cost)
            edges.append((start, end, cost))
            idx += 1
        test_cases.append((N, edges))

    results = solve(test_cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()