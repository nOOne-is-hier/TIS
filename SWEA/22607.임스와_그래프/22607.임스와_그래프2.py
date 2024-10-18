import heapq
from collections import defaultdict

def dijkstra(start, graph):
    distances = defaultdict(lambda: float('inf'))
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
        ims_graph = defaultdict(dict)
        banssafi_graph = defaultdict(dict)

        # Build the graph (directed edges, overwrite with latest cost if repeated)
        for x, y, cost in edges:
            ims_graph[x][y] = cost  # Directed edge for Imms
            banssafi_graph[x][y] = cost  # Reverse directed edge for BanSsafi

        # Run Dijkstra from 'a' and 'Z'
        ims_distances = dijkstra('a', ims_graph)
        banssafi_distances = dijkstra('Z', banssafi_graph)

        # Compare the distances from 'a' to 'Z' and 'Z' to 'a'
        ims_cost = ims_distances['Z']
        banssafi_cost = banssafi_distances['a']

        if ims_cost == float('inf') and banssafi_cost == float('inf'):
            results.append(f"#{t + 1} NO")
        elif ims_cost <= banssafi_cost:
            results.append(f"#{t + 1} YES {ims_cost}")
        else:
            results.append(f"#{t + 1} NO")

    return results

def main():
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