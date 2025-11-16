# 14938 – 서강그라운드
# https://www.acmicpc.net/problem/14938
# solved.ac: https://solved.ac/search?query=14938
# 시간 제한: 1 초
# 메모리 제한: 128 MB
# 티어: 🟡 Gold IV
# 태그: 그래프 이론, 데이크스트라, 최단 경로, 플로이드–워셜
# 푼 사람 수: 9,537
# 평균 시도: 1.98

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
    n, m, r = map(int, input().split())
    items = [0] + list(map(int, input().split()))
    dist = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for _ in range(r):
        a, b, l = map(int, input().split())
        dist[a][b] = l
        dist[b][a] = l

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print(
        max(
            sum(items[j] if dist[i][j] <= m else 0 for j in range(1, n + 1))
            for i in range(1, n + 1)
        )
    )


if __name__ == "__main__":
    main()
