import sys
sys.stdin = open('input.txt')
from collections import defaultdict

for tc in range(1, int(input()) + 1):
    N = int(input())
    # 각 알파벳의 가중치 관리
    costs = defaultdict(int)
    # 각 문자열 처리
    for _ in range(N):
        alphabets = input()
        length = len(alphabets)

        for idx in range(length):
            costs[alphabets[idx]] += 10 ** (length - idx - 1)

    costs = sorted(costs.items(), key=lambda x: x[1], reverse=True)

    # 결과 값을 저장할 변수
    result = 0
    num = 9
    while costs:
        _, value = costs.pop(0)
        value = list(str(value))
        digit = 0
        while value:
            result += int(value.pop()) * num * 10 ** digit
            digit += 1

        num -= 1

    print(f'#{tc} {result}')