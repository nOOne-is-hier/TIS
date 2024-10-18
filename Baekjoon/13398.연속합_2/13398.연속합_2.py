import sys

sys.stdin = open('input.txt')

# 입력 처리
n = int(input())
array = list(map(int, input().split()))

# DP 테이블 초기화
dp_no_remove = [0] * n  # 수를 제거하지 않은 경우
dp_remove = [0] * n  # 수를 하나 제거한 경우

# 초기값 설정
dp_no_remove[0] = array[0]
dp_remove[0] = -float('inf')  # 첫 번째 수는 제거할 수 없으므로 음의 무한대로 설정

# 카데인 알고리즘 적용
for i in range(1, n):
    # 수를 제거하지 않은 경우
    dp_no_remove[i] = max(dp_no_remove[i - 1] + array[i], array[i])

    # 수를 하나 제거한 경우
    dp_remove[i] = max(dp_remove[i - 1] + array[i], dp_no_remove[i - 1])

# 최종 답은 수를 제거한 경우와 제거하지 않은 경우 중 최대값
print(max(max(dp_no_remove), max(dp_remove)))
