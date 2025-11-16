# 2644 – 촌수계산
# https://www.acmicpc.net/problem/2644
# solved.ac: https://solved.ac/search?query=2644
# 시간 제한: 1 초
# 메모리 제한: 128 MB
# 티어: ⚪ Silver II
# 태그: 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 너비 우선 탐색
# 푼 사람 수: 26,655
# 평균 시도: 1.93

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
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    adjacency_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)

    dis = -1
    visited = [False] * (n + 1)

    def dfs(start, cnt):
        nonlocal dis

        if start == b:
            dis = cnt
            return

        if dis != -1:
            return

        for nxt in adjacency_list[start]:
            if not visited[nxt]:
                visited[nxt] = True
                dfs(nxt, cnt + 1)

    dfs(a, 0)

    print(dis)


if __name__ == "__main__":
    main()
