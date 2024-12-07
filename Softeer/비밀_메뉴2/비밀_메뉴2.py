import sys

sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
X = input().split()
Y = input().split()

dp = [[0] * (M + 1) for _ in range(N + 1)]
max_length = 0

for r in range(1, N + 1):
    for c in range(1, M + 1):
        if X[r - 1] == Y[c - 1]:
            dp[r][c] = dp[r - 1][c - 1] + 1
            max_length = max(max_length, dp[r][c])
        else:
            dp[r][c] = 0

print(max_length)
