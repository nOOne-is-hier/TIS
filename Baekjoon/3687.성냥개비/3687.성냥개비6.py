# python 31,120KB 56ms
import sys

sys.stdin = open('input.txt')

# 성냥개비 숫자에 대응되는 최소 성냥개비 개수
matchsticks = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}


# 최소값을 찾기 위한 동적 프로그래밍 함수
def find_min_case_dp(n):
    # DP 배열 초기화 (매우 큰 값으로 초기화)
    dp = ["inf"] * (n + 1)
    dp[0] = ""

    # 최소값 DP 채우기
    for i in range(2, n + 1):
        for number, match_count in matchsticks.items():
            if i - match_count >= 0:
                # 0은 제일 앞에 올 수 없으므로 예외 처리
                if number == 0 and dp[i - match_count] == "":
                    continue
                if dp[i - match_count] != "inf":
                    candidate = dp[i - match_count] + str(number)
                    if dp[i] == "inf" or int(candidate) < int(dp[i]):
                        dp[i] = candidate

    # DP[n] 값 반환
    return dp[n]


# 최대값을 찾기 위한 함수
def find_max_case_dp(n):
    # 최대값은 가능한 한 '1'을 많이 사용하는 것이 유리합니다.
    if n % 2 == 1:
        max_case = '7' + '1' * (n // 2 - 1)
    else:
        max_case = '1' * (n // 2)
    return max_case


# 입력 처리 및 결과 출력
T = int(input())
results = []
for _ in range(T):
    N = int(input())
    min_case = find_min_case_dp(N)
    max_case = find_max_case_dp(N)
    results.append(f"{min_case} {max_case}")

for result in results:
    print(result)
