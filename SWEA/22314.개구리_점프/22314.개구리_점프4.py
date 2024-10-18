class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 각 노드는 자기 자신을 부모로 가짐
        self.rank = [1] * n  # 모든 노드의 rank는 1로 초기화

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # 경로 압축
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def solve():
    # 첫 줄은 테스트 케이스 수
    T = int(input())

    for tc in range(1, T + 1):
        print(f"#{tc}", end=' ')

        # 통나무 수 N과 쿼리 수 Q 입력
        N, Q = map(int, input().split())

        # Union-Find 초기화
        uf = UnionFind(N + 1)

        # 통나무 구간 저장
        pond = [()] * (N + 1)
        for idx in range(1, N + 1):
            n_start, n_end, _ = map(int, input().split())  # y는 사용하지 않음
            pond[idx] = (n_start, n_end, idx)

        # 통나무의 시작점 기준으로 정렬
        pond.sort()

        # 병합 시작
        start_l, end_l, idx_l = pond[1]
        for cursor in range(2, N + 1):
            start_r, end_r, idx_r = pond[cursor]
            if start_l <= end_r and end_l >= start_r:
                uf.union(idx_l, idx_r)
            start_l = start_r
            end_l = end_r

        # 쿼리 처리 및 출력
        results = []
        for _ in range(Q):
            bar1, bar2 = map(int, input().split())
            if uf.find(bar1) == uf.find(bar2):
                results.append("1")
            else:
                results.append("0")

        # 결과 출력
        print(" ".join(results))


# 메인 함수 호출
solve()
