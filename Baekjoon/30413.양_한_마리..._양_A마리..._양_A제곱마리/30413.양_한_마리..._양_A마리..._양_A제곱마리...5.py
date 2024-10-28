import sys

sys.stdin = open('input.txt')


def power_recursive(ratio, exponent, divisior):
    nth_term = 1

    while exponent:
        if exponent % 2 == 1:
            nth_term *= ratio

        ratio **= 2
        ratio %= divisior
        exponent //= 2

    return nth_term % divisior


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
