def solution_dp(distance, rocks, n):
    rocks.sort()
    rocks = [0] + rocks + [distance]  # 시작점과 마지막 도착 지점을 추가합니다.
    dp = [[0] * (n + 1) for _ in range(len(rocks))]
    dp[0][0] = float('inf')  # 초기값 설정: 시작점에서의 최대 최소 거리

    for i in range(1, len(rocks)):
        for j in range(n + 1):
            # 바위를 제거하지 않는 경우
            if j <= i - 1:
                dp[i][j] = max(dp[i][j], min(dp[i - 1][j], rocks[i] - rocks[i - 1]))
            # 바위를 제거하는 경우 (제거 가능한 바위가 남아 있을 때)
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])

    return max(dp[-1])

# 예시 테스트
distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution_dp(distance, rocks, n))  # DP 풀이
