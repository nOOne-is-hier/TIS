# 15810 – 풍선 공장
# https://www.acmicpc.net/problem/15810
# solved.ac: https://solved.ac/search?query=15810
# 시간 제한: 1 초
# 메모리 제한: 256 MB
# 티어: ⚪ Silver II
# 태그: 매개 변수 탐색, 이분 탐색
# 푼 사람 수: 1,570
# 평균 시도: 3.42

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
    times = list(map(int, input().split()))
    l = 1
    r = 1e12
    result = 0
    while l <= r:
        mid = (l + r) // 2
        cnt = 0
        for t in times:
            cnt += mid // t

        if cnt >= M:
            result = mid
            r = mid - 1

        else:
            l = mid + 1

    print(int(result))


if __name__ == "__main__":
    main()
