import sys

sys.stdin = open('input.txt')

from collections import deque

n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [0] * n  # dp 배열 초기화

# 첫 계단에서 시작
dq = deque([(0, stairs[0], 1)])  # (현재 계단, 현재까지 비용, 연속 계단 수)

while dq:
    now, cost, cnt = dq.popleft()

    # dp[now]가 현재 비용보다 작더라도 계속 진행해야 함
    dp[now] = max(dp[now], cost)

    # 한 계단을 올라갈 경우 (연속으로 두 계단 이상은 밟을 수 없음)
    if now + 1 < n and cnt < 2:
        dq.append((now + 1, cost + stairs[now + 1], cnt + 1))

    # 두 계단을 올라갈 경우 (연속으로 세 계단을 밟지 않기 때문에 cnt를 1로 초기화)
    if now + 2 < n:
        dq.append((now + 2, cost + stairs[now + 2], 1))

# 결과 출력 (마지막 계단의 최댓값)
print(dp[n - 1])
