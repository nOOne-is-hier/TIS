import sys
import operator
sys.stdin = open('input.txt')


def DFS(current, idx, plus, minus, mul, div):
    global max_case, min_case

    # base case
    if idx == N:
        max_case = max(max_case, current)
        min_case = min(min_case, current)
        return current
    # 캐싱
    key = (current, idx, plus, minus, mul, div)
    if key in former_state:
        return former_state[key]

    # 연산자별로 가능한 연산 수행
    if plus > 0:
        DFS(operator.add(current, numbers[idx]), idx + 1, plus - 1, minus, mul, div)
    if minus > 0:
        DFS(operator.sub(current, numbers[idx]), idx + 1, plus, minus - 1, mul, div)
    if mul > 0:
        DFS(operator.mul(current, numbers[idx]), idx + 1, plus, minus, mul - 1, div)
    if div > 0:
        # 나눗셈은 정수 나눗셈 처리
        DFS(int(operator.truediv(current, numbers[idx])), idx + 1, plus, minus, mul, div - 1)

    former_state[key] = current
    return current


T = int(input())
results = []
for tc in range(1, T + 1):
    N = int(input())    # 숫자의 개수 3 <= N <= 12
    # 연산자 저장
    plus, minus, mul, div = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 초기값 설정
    max_case = -100000000
    min_case = 100000000
    # 메모이제이션
    former_state = {}
    # DFS 탐색
    DFS(numbers[0], 1, plus, minus, mul, div)

    results.append(f'#{tc} {max_case - min_case}')

print('\n'.join(results))
