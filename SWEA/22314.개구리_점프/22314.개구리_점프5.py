import sys
sys.stdin = open('input.txt')


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 각 노드는 자기 자신을 부모로 초기화
        self.rank = [1] * n  # 모든 원소의 rank를 1로 초기화

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # 경로 압축
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # rank가 낮은 쪽을 높은 쪽에 붙인다.
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


# 테스트 케이스 입력
for tc in range(1, int(input()) + 1):
    results = [f"#{tc}"]
    N, Q = map(int, input().split())

    # Union-Find 자료구조 생성
    uf = UnionFind(N)

    # 통나무들의 x1, x2 범위를 저장
    logs = []

    for idx in range(N):
        x1, x2, _ = map(int, input().split())  # y 좌표는 무시
        logs.append((x1, x2, idx))  # 통나무 번호도 같이 저장

    # 통나무의 시작점 기준으로 정렬
    logs.sort()  # x1을 기준으로 정렬

    # 통나무의 겹치는 구간을 확인하고 union 수행
    for i in range(1, N):
        prev_x1, prev_x2, prev_idx = logs[i - 1]
        curr_x1, curr_x2, curr_idx = logs[i]

        # 통나무가 겹치는지 확인: 이전 통나무의 끝점(prev_x2)이 현재 통나무의 시작점(curr_x1)보다 크거나 같으면 겹침
        if curr_x1 <= prev_x2:  # 겹친다면 두 통나무를 병합
            uf.union(prev_idx, curr_idx)
            # 현재 통나무의 끝점을 최대 끝점으로 업데이트
            logs[i] = (curr_x1, max(curr_x2, prev_x2), curr_idx)

    # 쿼리 처리
    for _ in range(Q):
        bar1, bar2 = map(int, input().split())
        # 통나무 번호는 1번부터 시작하므로 인덱스를 0 기반으로 변환
        if uf.find(bar1 - 1) == uf.find(bar2 - 1):
            results.append('1')
        else:
            results.append('0')

    # 결과 출력
    print(" ".join(results))
