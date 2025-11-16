# 1238 – 파티
# https://www.acmicpc.net/problem/1238
# solved.ac: https://solved.ac/search?query=1238
# 시간 제한: 1 초
# 메모리 제한: 128 MB
# 티어: 🟡 Gold III
# 태그: 그래프 이론, 데이크스트라, 최단 경로
# 푼 사람 수: 22,756
# 평균 시도: 1.99

import sys, io
from heapq import heappush, heappop


def input_stream():
    try:
        if not sys.stdin.isatty():
            return io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8", newline="")
    except Exception:
        pass
    try:
        return open("input.txt", "r", encoding="utf-8", newline="")
    except FileNotFoundError:
        return io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8", newline="")


def dijkstra(start, graph, N):
    dist = [int(1e9)] * (N + 1)
    dist[start] = 0
    pq = []
    heappush(pq, (0, start))

    while pq:
        cur_cost, u = heappop(pq)
        if cur_cost > dist[u]:
            continue

        for v, w in graph[u]:
            nxt_cost = cur_cost + w
            if nxt_cost < dist[v]:
                dist[v] = nxt_cost
                heappush(pq, (nxt_cost, v))

    return dist


def main() -> None:
    input = sys.stdin.readline
    N, M, X = map(int, input().split())
    adjacency_list = [[] for _ in range(N + 1)]
    reversed_adjacency_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v, w = map(int, input().split())
        adjacency_list[u].append((v, w))
        reversed_adjacency_list[v].append((u, w))

    dist1 = dijkstra(X, adjacency_list, N)
    dist2 = dijkstra(X, reversed_adjacency_list, N)

    print(max(dist1[i] + dist2[i] for i in range(1, N + 1)))


if __name__ == "__main__":
    main()
