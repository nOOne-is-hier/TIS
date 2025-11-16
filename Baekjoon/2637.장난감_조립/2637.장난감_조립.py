# 2637 – 장난감 조립
# https://www.acmicpc.net/problem/2637
# solved.ac: https://solved.ac/search?query=2637
# 시간 제한: 1 초
# 메모리 제한: 128 MB
# 티어: 🟡 Gold II
# 태그: 그래프 이론, 다이나믹 프로그래밍, 방향 비순환 그래프, 위상 정렬
# 푼 사람 수: 3,699
# 평균 시도: 2.01

import sys, io
from collections import deque


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


def main() -> None:
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    adjacency_list = [[] for _ in range(N + 1)]
    in_degrees = [0] * (N + 1)

    for _ in range(M):
        X, Y, K = map(int, input().split())
        in_degrees[X] += 1
        adjacency_list[Y].append((X, K))

    basic = []
    for i in range(1, N + 1):
        if in_degrees[i] == 0:
            basic.append(i)

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for b in basic:
        dp[b][b] = 1

    q = deque(basic)

    while q:
        cur = q.popleft()
        for nxt, k in adjacency_list[cur]:
            for b in basic:
                dp[nxt][b] += dp[cur][b] * k

            in_degrees[nxt] -= 1
            if in_degrees[nxt] == 0:
                q.append(nxt)

    for b in basic:
        if dp[N][b] > 0:
            print(b, dp[N][b])


if __name__ == "__main__":
    main()
