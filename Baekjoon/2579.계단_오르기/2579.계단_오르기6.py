import sys

sys.stdin = open('input.txt')

from collections import deque

n = int(input())  # 계단의 개수 입력
stairs = [int(input()) for _ in range(n)]  # 각 계단의 점수 입력
dp = [0] * n  # dp 배열 초기화, 각 계단에 도달할 수 있는 최대 점수 저장

# BFS를 위한 큐 초기화 (현재 계단, 현재까지의 점수, 연속 밟은 계단 수)
dq = deque([(0, stairs[0], 1)])  # 첫 번째 계단에서 시작
dp[0] = stairs[0]  # 첫 계단의 점수는 미리 설정

if n > 1:
    dq.append((1, stairs[0] + stairs[1], 2))  # 두 번째 계단에서 시작할 경우 추가
    dp[1] = stairs[0] + stairs[1]

# BFS 탐색 시작
while dq:
    now, cost, cnt = dq.popleft()

    # 현재까지의 cost로 dp 갱신
    dp[now] = max(dp[now], cost)

    # 한 칸을 올라가는 경우 (연속으로 두 개 이상 밟지 않기)
    if now + 1 < n and cnt < 2:
        next_cost = cost + stairs[now + 1]
        dq.append((now + 1, next_cost, cnt + 1))  # 한 칸 이동, 연속으로 밟은 횟수 증가

    # 두 칸을 올라가는 경우 (연속 칸 수 리셋)
    if now + 2 < n:
        next_cost = cost + stairs[now + 2]
        dq.append((now + 2, next_cost, 1))  # 두 칸 이동, 연속으로 밟은 횟수 리셋

# 마지막 계단에 도착했을 때의 최대 점수를 출력
print(dp[n - 1])
