import sys

sys.stdin = open('input.txt')


N = int(input())
stairs = [int(input()) for _ in range(N)]
scores = [0] * N
scores[0] = stairs[0]
if N > 1:
    scores[1] = stairs[0] + stairs[1]
if N > 2:
    scores[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for idx in range(3, N):
    scores[idx] = max(scores[idx - 2] + stairs[idx], scores[idx - 3] + stairs[idx - 1] + stairs[idx])

print(scores[N - 1])
