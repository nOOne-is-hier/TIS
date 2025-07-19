# 개미 (10158)
# https://www.acmicpc.net/problem/10158

import sys

def main() -> None:
    # 입력 최적화
    sys.stdin = open("input.txt", "r")
    input = sys.stdin.readline

    w, h = map(int, input().split())
    p, q = map(int, input().split())
    t = int(input())

    w_t = (t + p) % (2 * w) if w >= (t + p) % (2 * w) else w * 2 - ((t + p) % (2 * w))
    h_t = (t + q) % (2 * h) if h >= (t + q) % (2 * h) else h * 2 - ((t + q) % (2 * h))

    print(w_t, h_t)

if __name__ == "__main__":
    main()
