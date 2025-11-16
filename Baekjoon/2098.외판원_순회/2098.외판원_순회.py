# 2098 – 외판원 순회
# https://www.acmicpc.net/problem/2098
# solved.ac: https://solved.ac/search?query=2098
# 시간 제한: 1 초
# 메모리 제한: 128 MB
# 티어: 🟡 Gold I
# 태그: 다이나믹 프로그래밍, 비트마스킹, 비트필드를 이용한 다이나믹 프로그래밍, 외판원 순회 문제
# 푼 사람 수: 11,978
# 평균 시도: 3.50

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


def main() -> None:
    input = sys.stdin.readline
    N = int(input())
    dist = [list(map(int, input().split())) for _ in range(N)]
    dp = [[int(1e9)] * (1 << (N - 1)) for _ in range(N)]
    dp[0][0] = 0

    for mask in range(1 << (N - 1)):
        for cur in range(N):
            if dp[cur][mask] == int(1e9):
                continue
            for nxt in range(1, N):
                bit = 1 << (nxt - 1)
                if mask & bit:
                    continue
                if dist[cur][nxt] == 0:
                    continue
                new_mask = mask | bit
                dp[nxt][new_mask] = min(
                    dp[nxt][new_mask], dp[cur][mask] + dist[cur][nxt]
                )

    result = 1e9
    for cur in range(N):
        if dp[cur][(1 << (N - 1)) - 1] == 1e9 or dist[cur][0] == 0:
            continue
        result = min(result, dp[cur][(1 << (N - 1)) - 1] + dist[cur][0])

    print(result if result < 1e9 else 0)


if __name__ == "__main__":
    main()
