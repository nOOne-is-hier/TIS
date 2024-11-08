import sys

sys.stdin = open('input.txt')

N = int(input())
new_house = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

dp[0][1][0] = 1

for r in range(N):
    for c in range(2, N):
        if new_house[r][c]:
            continue
        dp[r][c][0] = dp[r][c - 1][0] + dp[r][c - 1][2]
        dp[r][c][1] = dp[r - 1][c][1] + dp[r - 1][c][2]
        if new_house[r - 1][c] or new_house[r][c - 1]:
            continue
        dp[r][c][2] = sum(dp[r - 1][c - 1])
print(sum(dp[N - 1][N - 1]))