import sys
sys.stdin = open('input.txt')
from collections import Counter


def find_min_case(num):
    count_numbers = Counter()
    count_numbers['8'] = num // 7
    num %= 7
    count_numbers['0'] = num // 6
    num %= 6
    count_numbers['2'] = num // 5
    num %= 5
    count_numbers['4'] = num // 4
    num %= 4
    count_numbers['7'] = num // 3
    num %= 3
    count_numbers['1'] = num // 2
    num %= 2
    if num == 1:
        count_numbers['8'] -= 1
        count_numbers['0'] += 1
        count_numbers['1'] += 1
    sorted_count_numbers = dict(sorted(count_numbers.items()))
    print(sorted_count_numbers)
    min_case = ''
    for number in sorted_count_numbers:
        if sorted_count_numbers[number]:
            min_case += number * sorted_count_numbers[number]
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