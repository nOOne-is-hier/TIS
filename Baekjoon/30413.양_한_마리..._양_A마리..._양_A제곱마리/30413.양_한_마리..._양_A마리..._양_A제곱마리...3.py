import sys

sys.stdin = open('input.txt')

A, B = map(int, input().split())
divisor = 10 ** 9 + 7
base = A

# A의 B승을 모듈러 연산으로 계산
A = pow(A, B, divisor)

# 공비수열의 합 공식 적용
if A == 1:
    # A가 1일 때는 모든 항이 1이므로 합은 B가 됩니다.
    result = B % divisor
else:
    # A^B - 1의 값을 계산하고, A - 1의 모듈러 역원을 곱하여 나눗셈을 처리
    numerator = (A - 1) % divisor
    denominator_inv = pow(base - 1, divisor - 2, divisor)  # 모듈러 역원 계산
    result = (numerator * denominator_inv) % divisor

print(result)
