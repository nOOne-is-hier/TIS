# 1647 – 도시 분할 계획
# https://www.acmicpc.net/problem/1647
# solved.ac: https://solved.ac/search?query=1647
# 시간 제한: 2 초
# 메모리 제한: 256 MB
# 티어: 🟡 Gold IV
# 태그: 그래프 이론, 최소 스패닝 트리
# 푼 사람 수: 14,115
# 평균 시도: 2.01

import sys, io


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


class DSU:
    def __init__(self, N) -> None:
        self.parent = list(range(N + 1))
        self.rank = [0] * (N + 1)

    def find(self, x) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, a, b) -> bool:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True


def main() -> None:
    input = sys.stdin.readline
    N, M = map(int, input().split())
    edge_list = [(0, 0, 0)] * M
    for i in range(M):
        A, B, C = map(int, input().split())
        edge_list[i] = (C, A, B)

    edge_list.sort()

    dsu = DSU(N)

    result = cnt = 0

    for cost, u, v in edge_list:
        if cnt == N - 2:
            break
        if dsu.unite(u, v):
            result += cost
            cnt += 1

    print(result)


if __name__ == "__main__":
    main()
