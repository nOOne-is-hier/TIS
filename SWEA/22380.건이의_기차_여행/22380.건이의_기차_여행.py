import sys
sys.stdin = open('input.txt')
import heapq

INF = float('inf')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    N, T = map(int, input().split())
    # 인접 리스트
    adjacency_list = [[] for _ in range(N + 1)]
    # 간선 추가
    for _ in range(T):
        a, b, w = map(int, input().split())
        adjacency_list[a] += [(b, w)]
    # 비용을 추적할 list
    min_cost = [0] + [INF] * N
    orders = [(0, 0)]
    
    # 다익스트라 알고리즘 시작
    while orders:
        current_cost, current_node = heapq.heappop(orders)
        # 최소 비용이 아니라면 pass
        if current_cost > min_cost[current_node]:
            continue
        # 현재 노드의 모든 간선 확인
        for next_node, cost in adjacency_list[current_node]:
            next_cost = current_cost + cost

            # 더 적은 비용으로 다음 노드에 갈 수 있다면 갱신
            if min_cost[next_node] > next_cost:
                min_cost[next_node] = next_cost
                heapq.heappush(orders, (next_cost, next_node))

    if min_cost[N - 1] == INF:
        print('impossible')
    else:
        print(min_cost[N - 1])