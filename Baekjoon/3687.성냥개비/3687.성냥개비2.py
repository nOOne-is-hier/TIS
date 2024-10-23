import sys
sys.stdin = open('input.txt')
from collections import Counter

delta = {7: '8', 6: '0', 5: '2', 4: '4', 3: '7', 2: '1'}


def find_min_case(num):
    # dp[i]는 i개의 성냥개비로 만들 수 있는 최소 숫자
    dp = [''] * (num + 1)
    dp[0] = dp[1] = 0
    for divisor in delta:
        if num >= divisor and dp[num - divisor] != '':
            candidate = str(dp[num - divisor]) + delta[divisor]
            # 가장 작은 숫자가 되도록 정렬하여 최소값을 유지
            if dp[num] == '' or int(''.join(sorted(candidate))) < int(''.join(sorted(dp[num]))):
                dp[num] = candidate

    # 최종적으로 dp[num]에 저장된 값이 최소값
    min_case = ''.join(sorted(dp[num]))
    print(dp)

    # 첫 번째 자리가 0이면, 가장 앞자리를 0이 아닌 값으로 바꿈
    if min_case and min_case[0] == '0':
        min_case = list(min_case)
        for idx in range(1, len(min_case)):
            if min_case[idx] != '0':
                min_case[0], min_case[idx] = min_case[idx], min_case[0]
                break
        min_case = ''.join(min_case)

    return min_case


def find_max_case(num):
    max_case = ''
    count_numbers = Counter()
    count_numbers['1'] = num // 2
    num %= 2
    if num == 1:
        count_numbers['1'] -= 1
        max_case += '7'
        max_case += '1' * count_numbers['1']
    else:
        max_case += '1' * count_numbers['1']

    return max_case


T = int(input())

for tc in range(T):
    N = int(input())
    min_case = find_min_case(N)
    max_case = find_max_case(N)

    print(min_case, max_case)