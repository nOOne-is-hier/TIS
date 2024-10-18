import sys

sys.stdin = open('input.txt')

# 비트마스크를 이용한 계단 오르기 문제
def find_max_score(start=0, state=0, current_score=0):
    # base case: 마지막 계단에 도달했을 때
    if start == N - 1:
        return current_score

    # 메모이제이션 체크
    if memo[state] != -1:
        return memo[state]

    max_value = 0

    # 현재 상태에서 마지막 2비트를 확인 (연속된 1이 있는지 체크)
    if (state & 3) != 3:  # 연속된 1이 없다면 (비트마스크의 마지막 두 비트가 11이 아닌 경우)
        if start + 1 < N:  # 1칸 이동 가능
            new_state = ((state << 1) | 1) & ((1 << N) - 1)  # 새로운 상태로 1을 추가
            max_value = max(max_value, find_max_score(start + 1, new_state, current_score + stairs[start + 1]))

    # 2칸 이동은 언제나 가능
    if start + 2 < N:
        new_state = (state << 2) & ((1 << N) - 1)  # 새로운 상태로 2비트를 이동
        max_value = max(max_value, find_max_score(start + 2, new_state, current_score + stairs[start + 2]))

    # 메모이제이션 저장
    memo[state] = max_value
    return max_value

# 입력 처리
N = int(input())
stairs = [int(input()) for _ in range(N)]

# 메모이제이션 배열 초기화 (-1로 초기화하여 아직 계산되지 않은 상태로 설정)
memo = [-1] * (2 ** N)

# 결과 계산
result = find_max_score()
print(result)