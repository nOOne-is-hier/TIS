import sys
sys.stdin = open('input.txt')

delta = {7: '8', 6: '0', 5: '2', 4: '4', 3: '7', 2: '1'}

def find_min_cases(num, case=None, max_length=None):
    if max_length is None:
        max_length = [50]

    if case is None:
        case = []

    key = (num, tuple(case))
    if key in memo:
        return
    memo.add(key)

    # 특수 처리된 값들에 대한 간소화된 처리
    if num == 11:
        min_cases.append(case + ['0', '2'])
        return
    if num == 10:
        min_cases.append(case + ['5', '5'])
        return
    if num == 9:
        min_cases.append(case + ['8', '1'])
        return
    if num == 8:
        min_cases.append(case + ['0', '1'])
        return

    if num == 0:
        min_cases.append(case[:])
        max_length[0] = len(case)
        return

    if len(case) >= max_length[0]:
        return

    for number in delta:
        if num >= number:
            case.append(delta[number])
            find_min_cases(num - number, case, max_length)
            case.pop()

def find_min_case(cases):
    min_case = float('inf')
    for case in cases:
        if case[0] == '0':
            for idx in range(1, len(case)):
                if case[idx] != '0':
                    case[0], case[idx] = case[idx], case[0]
                    break
            else:
                case[0] = '6'
        tmp_sum = int(''.join(case))
        if tmp_sum:
            min_case = min(min_case, tmp_sum)
    return min_case

def find_max_case(num):
    max_case = '7' if num % 2 == 1 else ''
    max_case += '1' * (num // 2 - (num % 2))
    return max_case

T = int(input())
for tc in range(T):
    N = int(input())
    min_cases = []
    memo = set()
    find_min_cases(N)
    min_case = find_min_case(min_cases)
    max_case = find_max_case(N)

    print(min_case, max_case)
