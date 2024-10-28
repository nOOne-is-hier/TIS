import sys

sys.stdin = open('input.txt')


def power_recursive(ratio, exponent, divisior):
    if exponent == 1:
        return ratio % divisior

    half_power = power_recursive(ratio, exponent // 2, divisior)
    half_power = (half_power * half_power) % divisior

    if exponent % 2 != 0:
        half_power = (half_power * ratio) % divisior

    return half_power


A, B = map(int, input().split())
divisor = 10 ** 9 + 7
base = A

# A의 B승을 모듈러 연산으로 계산
if A == 1:
    result = B % divisor
else:
    A = power_recursive(A, B, divisor)

    # A^B - 1의 값을 계산하고, A - 1의 모듈러 역원을 곱하여 나눗셈을 처리
    numerator = (A - 1)
    denominator_inv = power_recursive(base - 1, divisor - 2, divisor)  # 모듈러 역원 계산
    result = (numerator * denominator_inv) % divisor

print(result)
