import sys
sys.stdin = open('input.txt')
from collections import deque

# 필름이 합격 기준을 충족하는지 검증 (비트마스크 방식)
def is_qualified(state_bits):
    for c in range(W):  # 각 열에 대해 탐색
        current_streak = 1  # 현재 연속된 값의 길이
        for r in range(1, D):  # 1행부터 마지막 행까지 비교
            current_bit = (state_bits[r] >> c) & 1
            previous_bit = (state_bits[r - 1] >> c) & 1
            if current_bit == previous_bit:
                current_streak += 1
            else:
                current_streak = 1

            if current_streak >= K:
                break
        if current_streak < K:
            return False
    return True

# BFS 탐색을 통해 최소 약품 투입 횟수 찾기 (비트마스크 방식)
def BFS(initial_state):
    queue = deque([(initial_state, 0)])  # 필름 상태, 약품 투입 횟수
    visited = set()

    if is_qualified(initial_state):
        return 0

    while queue:
        state_bits, count = queue.popleft()

        state_tuple = tuple(state_bits)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for row in range(D):
            # 약품 A(0)를 투입한 경우 (해당 행을 0으로)
            new_state_A = state_bits[:]
            new_state_A[row] = 0
            if is_qualified(new_state_A):
                return count + 1
            queue.append((new_state_A, count + 1))

            # 약품 B(1)을 투입한 경우 (해당 행을 1로)
            new_state_B = state_bits[:]
            new_state_B[row] = (1 << W) - 1  # W개의 1로 채운 비트마스크
            if is_qualified(new_state_B):
                return count + 1
            queue.append((new_state_B, count + 1))

    return -1

# 입력 처리
T = int(input())

for tc in range(1, T + 1):
    D, W, K = map(int, input().split())  # 두께, 폭, 합격기준
    film = [int(''.join(map(str, input().split())), 2) for _ in range(D)]  # 필름 정보

    # BFS를 통해 최소 약품 투입 횟수 계산
    result = BFS(film)

    # 출력
    print(f'#{tc} {result}')
