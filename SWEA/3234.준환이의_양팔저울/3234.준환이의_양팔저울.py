import sys
sys.stdin = open('input.txt')

# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     weights = list(map(int, input().split()))


def solve(N, weights):
    total_weight = sum(weights)
    max_weight = total_weight + 1
    dp = [[0] * max_weight for _ in range(1 << N)]
    dp[0][0] = 1

    for mask in range(1 << N):
        for left in range(total_weight + 1):
            if dp[mask][left] == 0:
                continue
            right = sum(weights[i] for i in range(N) if mask & (1 << i)) - left
            for i in range(N):
                if mask & (1 << i) == 0:  # 무게추 i가 아직 사용되지 않은 경우
                    new_mask = mask | (1 << i)
                    # 왼쪽에 추가하는 경우
                    dp[new_mask][left + weights[i]] += dp[mask][left]
                    # 오른쪽에 추가하는 경우, 조건 확인
                    if left >= right + weights[i]:
                        dp[new_mask][left] += dp[mask][left]

    return sum(dp[(1 << N) - 1])


# 입력 처리
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    result = solve(N, weights)
    print(f'#{tc} {result}')
