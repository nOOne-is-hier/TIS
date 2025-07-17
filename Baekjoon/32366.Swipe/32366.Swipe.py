# Swipe (32366)
# https://www.acmicpc.net/problem/32366

import sys

def main() -> None:
    # 입력 최적화
    sys.stdin = open("input.txt", "r")
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    compressed_b = []
    segments = []
    l = 0
    for i in range(1, N):
        if B[i] != B[i - 1]:
            compressed_b.append(B[l])
            segments.append((l, i - 1))
            l = i
    compressed_b.append(B[l])
    segments.append((l, N - 1))
    elems = len(compressed_b)

    points = [-1] * elems
    i = j = 0
    while i < N and j < elems:
        if A[i] == compressed_b[j]:
            points[j] = i
            j += 1
        i += 1

    if j < elems:
        print("NO")
        return
    
    L_queries, R_queries = [], []
    for i in range(elems):
        l, r = segments[i]
        j = points[i]
        if j > l:
            L_queries.append(("L", l, j))
        if j < r:
            R_queries.append(("R", j, r))

    queries = L_queries + R_queries[::-1]
    print("YES")
    print(len(queries))
    for d, l, r in queries:
        print(d, l, r)

if __name__ == "__main__":
    main()
