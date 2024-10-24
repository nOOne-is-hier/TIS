# python 31,120KB 36ms
import sys

sys.stdin = open('input.txt')

# 최대값을 찾기 위한 함수 (Greedy 방식 그대로 구현)
def find_max_case_greedy(n):
    high = ''
    a = n // 2
    b = n % 2
    for _ in range(a):
        high += '1'
    if b == 1:
        high = '7' + high[:-1]
    return high

# 최소값을 찾기 위한 함수 (Greedy 방식 그대로 구현)
def find_min_case_greedy(n):
    low = ''
    low_case = ['0', '0', '1', '7', '4', '2', '6']
    if n < 7:
        low = low_case[n]
    else:
        a = n // 7
        b = n % 7
        for _ in range(a):
            low += '8'
        if 0 < b <= 2:
            for i in range(2 - b):
                low = '0' + low[:-1]
            low = '1' + low
        elif 2 < b < 6:
            for i in range(5 - b):
                low = '0' + low[:-1]
            if (5 - b) > len(low):
                low = low[:-1] + low_case[6 - ((5 - b) - len(low))]
            low = '2' + low
        elif b == 6:
            low = '6' + low
    return low

# 입력 처리 및 결과 출력
case_num = int(input())
results = []
for _ in range(case_num):
    n = int(input())
    min_case = find_min_case_greedy(n)
    max_case = find_max_case_greedy(n)
    results.append(f"{min_case} {max_case}")

for result in results:
    print(result)
