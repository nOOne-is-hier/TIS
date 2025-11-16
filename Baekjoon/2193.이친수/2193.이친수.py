# 2193 – 이친수
# https://www.acmicpc.net/problem/2193
# solved.ac: https://solved.ac/search?query=2193
# 시간 제한: 2 초
# 메모리 제한: 128 MB
# 티어: ⚪ Silver III
# 태그: 다이나믹 프로그래밍
# 푼 사람 수: 38,150
# 평균 시도: 2.38

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
    N = int(input())
    dp = [[0] * N for _ in range(2)]
    dp[1][0] = 1

    for i in range(1, N):
        dp[0][i] = dp[0][i - 1] + dp[1][i - 1]
        dp[1][i] = dp[0][i - 1]

    print(dp[0][N - 1] + dp[1][N - 1])


if __name__ == "__main__":
    main()
