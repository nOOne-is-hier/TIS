import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')


def dijkstra_pairwise(first, second):
    # 타임스탬프
    global current_time
    current_time += 1
    timestamp[first] = timestamp[second] = current_time

    # 방문 처리
    is_visited = [20000] * N
    is_visited[first] = is_visited[second] = 0

    order = [(0, first), (0, second)]
    while order:
        distance, last_node = heappop(order)

        for next_node in adjacency_list[last_node]:
            if timestamp[next_node] != current_time:
                if distance + 1 < is_visited[next_node]:
                    is_visited[next_node] = distance + 1
                    heappush(order, (distance + 1, next_node))
                timestamp[next_node] = current_time

    total_distance = 2 * sum(is_visited)

    return total_distance


N, M = map(int, input().split())

adjacency_list = [[] for _ in range(N)]

# 방문 리스트 대신 타임스탬프 사용
timestamp = [-1] * N
current_time = 0

for _ in range(M):
    A, B = map(int, input().split())
    adjacency_list[A - 1].append(B - 1)
    adjacency_list[B - 1].append(A - 1)

tmp_result = (20000, 100, 100)
for first in range(N):
    for second in range(first + 1, N):
        case = dijkstra_pairwise(first, second)
        tmp_result = min((case, first + 1, second + 1), tmp_result)

print(f'{tmp_result[1]} {tmp_result[2]} {tmp_result[0]}')