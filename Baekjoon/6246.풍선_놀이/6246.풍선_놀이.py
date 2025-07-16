# 풍선 놀이 (6246)
# https://www.acmicpc.net/problem/6246

import sys

def main() -> None:
    # 입력 최적화
    sys.stdin = open("input.txt", "r")
    input = sys.stdin.readline

    N, Q = map(int, input().split())

    slots = [False] * N

    for i in range(Q):
        L, I = map(int, input().split())

        while (L <= N):
            slots[L-1] = True
            L += I

    print(sum(1 for slot in slots if not slot))

if __name__ == "__main__":
    main()
