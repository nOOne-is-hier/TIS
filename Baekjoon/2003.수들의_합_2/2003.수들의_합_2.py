# 2003 – 수들의 합 2
# https://www.acmicpc.net/problem/2003
# solved.ac: https://solved.ac/search?query=2003
# 시간 제한: 0.5 초
# 메모리 제한: 128 MB
# 티어: ⚪ Silver IV
# 태그: 누적 합, 두 포인터, 브루트포스 알고리즘
# 푼 사람 수: 24,286
# 평균 시도: 2.05

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
    N, M = map(int, input().split())
    sequence = list(map(int, input().split()))

    l = r = tmp = result = 0

    while True:
        if tmp >= M:
            if tmp == M:
                result += 1
            tmp -= sequence[l]
            l += 1

        elif r == N:
            break

        else:
            tmp += sequence[r]
            r += 1

    print(result)


if __name__ == "__main__":
    main()
