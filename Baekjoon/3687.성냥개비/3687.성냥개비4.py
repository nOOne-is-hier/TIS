# python 34,192KB	52ms
import sys
sys.stdin = open('input.txt')
from collections import Counter

delta = {7: '8', 6: '0', 5: '2', 4: '4', 3: '7', 2: '1'}
sub_delta = {13: '68', 11: '02', 10: '22', 9: '81', 8: '01'}


def for_exceptions(num, multiplier, counter):
    if num + multiplier in sub_delta:
        if counter[delta[multiplier]]:
            counter[delta[multiplier]] -= 1
        for divisor in sub_delta[num + multiplier]:
            counter[divisor] += 1
        return 0
    return num

def find_min_case(num):

    # 일반적인 숫자 분해 로직
    count_numbers = Counter()
    if num >= 7:
        count_numbers['8'] = num // 7
        num %= 7
        num = for_exceptions(num, 7, count_numbers)

    if num >= 6:
        count_numbers['0'] = num // 6
        num %= 6
        num = for_exceptions(num, 6, count_numbers)

    if num >= 5:
        count_numbers['2'] = num // 5
        num %= 5
        num = for_exceptions(num, 5, count_numbers)

    if num >= 4:
        count_numbers['4'] = num // 4
        num %= 4
        num = for_exceptions(num, 4, count_numbers)

    if num >= 3:
        count_numbers['7'] = num // 3
        num %= 3
        num = for_exceptions(num, 3, count_numbers)

    if num >= 2:
        count_numbers['1'] = num // 2
        num %= 2
        num = for_exceptions(num, 2, count_numbers)

    # 숫자 정렬 및 문자열 생성
    sorted_count_numbers = dict(sorted(count_numbers.items()))
    min_case = ''
    for number in sorted_count_numbers:
        if sorted_count_numbers[number]:
            min_case += number * sorted_count_numbers[number]

    # 0 처리
    if len(min_case) >= 3 and all(x in min_case for x in ('2', '8')) and not '0' in min_case and min_case.count('2') > 1:
        tmp_case = list(min_case)
        tmp_case.remove('2')
        tmp_case.remove('8')
        tmp_case.append('0')
        tmp_case.append('0')
        tmp_case.sort()
        min_case = ''.join(tmp_case)

    if min_case == '0':
        min_case = '6'

    elif min_case[0] == '0':
        min_case = list(min_case)
        for idx in range(1, len(min_case)):
            if min_case[idx] != '0':
                min_case[0], min_case[idx] = min_case[idx], min_case[0]
                min_case = ''.join(min_case)
                break

    return min_case


def find_max_case(num):
    max_case = '7' if num % 2 == 1 else ''
    max_case += '1' * (num // 2 - (num % 2))
    return max_case

T = int(input())
results = []
for tc in range(T):
    N = int(input())
    min_case = find_min_case(N)
    max_case = find_max_case(N)
    results.append(min_case)
    results.append(max_case)

for idx in range(T):
    print(f'{results[idx * 2]},', end=' ')
    print(f'{results[idx * 2 + 1]},')
