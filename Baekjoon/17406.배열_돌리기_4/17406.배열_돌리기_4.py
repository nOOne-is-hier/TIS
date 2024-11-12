import sys
from itertools import permutations

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = tuple(tuple(map(int, input().split())) for _ in range(N))
calculations = tuple(tuple(map(int, input().split())) for _ in range(K))

tmp_min = 5000
for perm in permutations(calculations):
    new_grid = [list(row) for row in grid]
    former_gird = [row[:] for row in new_grid]
    for r, c, s in perm:

        for dis in range(1, s + 1):
            top, left, right, bottom = r - dis - 1, c - dis - 1, c + dis - 1, r + dis - 1

            for idx in range(left, right):
                new_grid[top][idx + 1] = former_gird[top][idx]
            for idx in range(top, bottom):
                new_grid[idx + 1][right] = former_gird[idx][right]
            for idx in range(right, left, -1):
                new_grid[bottom][idx - 1] = former_gird[bottom][idx]
            for idx in range(bottom, top, -1):
                new_grid[idx - 1][left] = former_gird[idx][left]

        former_gird = [row[:] for row in new_grid]

    tmp_min = min(tmp_min, min(sum(row) for row in new_grid))
print(tmp_min)