import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs_has_cycle(graph, N):
    visited = [False] * N  # 각 노드의 방문 여부

    for start in range(N):
        if not visited[start]:  # 방문하지 않은 노드에 대해 BFS 수행
            queue = deque([(start, -1)])  # (노드, 부모 노드) 저장
            visited[start] = True

            while queue:
                node, parent_node = queue.popleft()

                for neighbor in range(N):
                    if graph[node][neighbor] == 1:  # 연결된 노드 찾기
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append((neighbor, node))  # 큐에 (노드, 부모) 추가
                        elif neighbor != parent_node:
                            # 이미 방문한 노드가 부모 노드가 아니면 순환이 존재
                            return True
    return False


# 테스트 케이스 처리
T = int(input())  # 테스트 케이스의 수

for t in range(1, T + 1):
    N = int(input())  # 노드의 개수
    graph = [list(map(int, input().split())) for _ in range(N)]  # 인접 행렬 입력 받기

    if bfs_has_cycle(graph, N):
        print(f"#{t} WARNING")
    else:
        print(f"#{t} STABLE")