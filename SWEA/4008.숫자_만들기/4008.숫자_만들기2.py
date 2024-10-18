import sys
import operator
import itertools
sys.stdin = open('input.txt')

# 숫자와 연산자를 매핑하는 딕셔너리
operator_mapping = {
    0: operator.add,  # + 연산자
    1: operator.sub,  # - 연산자
    2: operator.mul,  # * 연산자
    3: operator.truediv  # / 연산자 (먼저 일반 나눗셈을 하고, 결과를 정수로 변환)
}

T = int(input())
result = []
for tc in range(1, T + 1):

    N = int(input())  # 숫자의 개수 3 <= N <= 12
    # 연산자 저장
    operands = []
    for idx, token in enumerate(map(int, input().split())):
        operands.extend([idx] * token)

    # 숫자들
    numbers = list(map(int, input().split()))

    # 모든 연산자 경우의 수 (중복 제거)
    every_cases = set(itertools.permutations(operands, len(operands)))

    # 연산 시작
    max_case = -100000000
    min_case = 100000000

    for order in every_cases:
        current = numbers[0]
        for idx, token in enumerate(order):
            # 나눗셈의 경우 소수점 이하를 버리기 위해 int() 처리
            current = int(operator_mapping[token](current, numbers[idx + 1]))

        # 최대값과 최소값 갱신
        max_case = max(max_case, current)
        min_case = min(min_case, current)

    # 최대값과 최소값의 차이
    result.append(f'#{tc} {max_case - min_case}')

print('\n'.join(result))
