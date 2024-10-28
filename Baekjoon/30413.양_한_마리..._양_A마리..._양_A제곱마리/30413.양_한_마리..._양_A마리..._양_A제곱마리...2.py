import sys

sys.stdin = open('input.txt')

A, B = map(int, input().split())
divisor = 10 ** 9 + 7

# 공비수열의 합을 for loop로 계산
result = 0
current_term = 1  # 첫 번째 항 (A^0 = 1)

for _ in range(B):
    result = (result + current_term) % divisor  # 현재 항을 합에 추가
    current_term = (current_term * A) % divisor  # 다음 항 계산

print(result)
