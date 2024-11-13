from collections import deque

for tc in range(1, 11):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))

    # 인접 리스트 및 진입 차수 배열 생성
    adjacency_list = [[] for _ in range(V + 1)]
    in_degrees = [0] * (V + 1)
    for i in range(E):
        pre, sub = edges[i * 2], edges[i * 2 + 1]
        adjacency_list[pre].append(sub)
        in_degrees[sub] += 1

    # 초기 진입 차수 0인 노드 큐에 추가
    order = deque([i for i in range(1, V + 1) if in_degrees[i] == 0])
    result = []

    while order:
        node = order.popleft()
        result.append(node)
        for next_node in adjacency_list[node]:
            in_degrees[next_node] -= 1
            if in_degrees[next_node] == 0:
                order.append(next_node)

    # 결과 출력
    print(f'#{tc}', *result)
