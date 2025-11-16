# 7795 – 먹을 것인가 먹힐 것인가
# https://www.acmicpc.net/problem/7795
# solved.ac: https://solved.ac/search?query=7795
# 시간 제한: 1 초
# 메모리 제한: 256 MB
# 티어: ⚪ Silver III
# 태그: 두 포인터, 이분 탐색, 정렬
# 푼 사람 수: 8,580
# 평균 시도: 1.95

import sys, io, bisect


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

    T = int(input())
    for tc in range(T):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        B.sort()
        result = 0
        for a in A:
            result += bisect.bisect_left(B, a)
        print(result)


if __name__ == "__main__":
    main()
