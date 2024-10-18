import heapq


def dijkstra(graph, start):
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


def solve_test_case(edges, n):
    graph = {}
    nodes = set()

    for start, end, cost in edges:
        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}

        if end in graph[start]:
            graph[start][end] = min(graph[start][end], cost)
        else:
            graph[start][end] = cost

        nodes.add(start)
        nodes.add(end)

    # Add default values to ensure all nodes are reachable
    for node in nodes:
        if node not in graph:
            graph[node] = {}

    ims_distances = dijkstra(graph, 'a')
    banssafi_distances = dijkstra(graph, 'Z')

    ims_time = ims_distances.get('Z', float('inf'))
    banssafi_time = banssafi_distances.get('a', float('inf'))

    if ims_time <= banssafi_time and ims_time != float('inf'):
        return f"YES {ims_time}"
    else:
        return "NO"


def main():
    t = int(input())
    results = []

    for test_case_number in range(1, t + 1):
        n = int(input())
        edges = []

        for _ in range(n):
            start, end, cost = input().split()
            cost = int(cost)
            edges.append((start, end, cost))

        result = solve_test_case(edges, n)
        results.append(f"#{test_case_number} {result}")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()