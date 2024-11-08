import sys
from functools import lru_cache

sys.stdin = open('input.txt')

# 델타 배열
# 0: 가로 / 1: 세로 / 2: 대각선
dr = (0, 1, 1)
dc = (1, 0, 1)


def count_all_cases():
    @lru_cache(None)
    def dfs(r=0, c=1, state=0):
        if r == c == N - 1:
            return 1

        total_ways = 0
        for dir in range(3):
            if state != dir and not (dir == 2 or state == 2):
                continue
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0 <= nr < N and 0 <= nc < N and not new_house[nr][nc]:
                if dir == 2 and (new_house[nr - 1][nc] or new_house[nr][nc - 1]):
                    continue
                total_ways += dfs(nr, nc, dir)

        return total_ways

    return dfs()

N = int(input())
new_house = tuple(tuple(map(int, input().split())) for _ in range(N))
print(count_all_cases())