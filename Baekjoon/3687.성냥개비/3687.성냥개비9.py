# python 31,120KB 40ms
import sys

sys.stdin = open('input.txt')

# 성냥개비 숫자에 대응되는 최소 성냥개비 개수
matchsticks = {0: 6, 1: 2, 2: 5, 4: 4, 6: 6, 7: 3, 8: 7}

# 최소값을 찾기 위한 동적 프로그래밍 함수
# DP 배열 초기화 (매우 큰 값으로 초기화)
dp = [["inf"] * 101 for _ in range(2)]
dp[0][0] = ""

# 13 이하의 경우를 하드코딩
dp[0][2] = '1'
dp[0][3] = '7'
dp[0][4] = '4'
dp[0][5] = '2'
dp[0][6] = '6'
dp[0][7] = '8'
dp[0][8] = '10'
dp[0][9] = '18'
dp[0][10] = '22'
dp[0][11] = '20'
dp[0][12] = '28'
dp[0][13] = '68'

# 최소값 DP 채우기
for i in range(101):
    if i > 13:
        for number, match_count in matchsticks.items():
            if i - match_count >= 0:
                # 0은 제일 앞에 올 수 없으므로 예외 처리
                if number == 0 and dp[0][i - match_count] == "":
                    continue
                if dp[0][i - match_count] != "inf":
                    candidate = dp[0][i - match_count] + str(number)
                    if dp[0][i] == "inf" or int(candidate) < int(dp[0][i]):
                        dp[0][i] = candidate
    max_case = ('7' if i % 2 == 1 else '1') + '1' * (i // 2 - 1)
    dp[1][i] = max_case

# 입력 처리 및 결과 출력
T = int(input())
for _ in range(T):
    N = int(input())
    min_case = dp[0][N]
    max_case = dp[1][N]
    print(min_case, max_case)
