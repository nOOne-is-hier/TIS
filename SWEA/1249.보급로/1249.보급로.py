import sys
sys.stdin = open('input.txt')


def DFS(r=0, c=0, current_cost=0, min_cost=None):
    # 최대 비용
    if not min_cost:
        min_cost = [(2 * N - 1) * 9]
    # 비용이 0이라면 종료
    if min_cost[0] == 0:
        return min_cost[0]
    # 현재 비용
    current_cost += ardennes[r][c]
    # 가지치기
    if current_cost >= min_cost[0]:
        return
    # 목적지 도착
    if r == c == N - 1:
        if min_cost[0] > current_cost:
            min_cost[0] = current_cost
    # 오른쪽으로 갈래
    if c + 1 < N:
        result = DFS(r, c + 1, current_cost, min_cost)
        if result == 0:
            return result
    # 아래로 갈래
    if r + 1 < N:
        result = DFS(r + 1, c, current_cost, min_cost)
        if result == 0:
            return result

    return min_cost[0]


for tc in range(1, int(input()) + 1):
    N = int(input())
    ardennes = [list(map(int, list(input()))) for _ in range(N)]

    print(DFS())