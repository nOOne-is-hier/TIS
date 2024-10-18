import sys
sys.stdin = open('input.txt')
from collections import deque


# 필름이 합격 기준을 충족하는지 검증
def is_qualified(state):
    for c in range(W):  # 각 열에 대해 탐색
        max_streak = 1  # 연속된 값의 최대 길이
        current_streak = 1  # 현재 연속된 값의 길이

        for r in range(1, D):  # 1행부터 마지막 행까지 비교
            if state[r][c] == state[r - 1][c]:
                current_streak += 1  # 연속된 값일 경우 streak 증가
            else:
                current_streak = 1  # 연속되지 않으면 streak 초기화

            max_streak = max(max_streak, current_streak)  # 최대 연속 값 갱신

            # 연속된 값이 K 이상이면 해당 열은 통과
            if max_streak >= K:
                break  # 이 열은 통과했으므로 다음 열로 넘어감

        # 만약 한 열에서 연속된 값이 K보다 작은 경우 False 반환
        if max_streak < K:
            return False

    return True


# 필름의 행에 약품을 투입하는 함수
def inject_chemical(row, chemical_type, state):
    # 필름의 해당 행을 약품으로 처리하여 새로운 상태 반환
    new_state = [row[:] for row in state]  # 깊은 복사
    for c in range(W):
        new_state[row][c] = chemical_type
    return new_state


# BFS 탐색을 통해 최소 약품 투입 횟수 찾기
def BFS(initial_state):
    queue = deque([(initial_state, 0)])  # 필름 상태, 약품 투입 횟수
    visited = set()  # 방문한 상태를 기록

    # 초기 상태에서 성능 검사 통과 여부 확인
    if is_qualified(initial_state):
        return 0

    # BFS 탐색 시작
    while queue:
        state, count = queue.popleft()

        # 만약 이미 방문한 상태면 무시
        state_tuple = tuple(map(tuple, state))
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        # 약품을 투입하지 않은 상태에서 탐색
        for row in range(D):
            # 약품 A(0)를 투입한 경우
            new_state_A = inject_chemical(row, 0, state)
            if is_qualified(new_state_A):
                return count + 1  # 성능검사 통과 시 최소 투입 횟수 반환
            queue.append((new_state_A, count + 1))

            # 약품 B(1)을 투입한 경우
            new_state_B = inject_chemical(row, 1, state)
            if is_qualified(new_state_B):
                return count + 1  # 성능검사 통과 시 최소 투입 횟수 반환
            queue.append((new_state_B, count + 1))

    return -1  # 만약 통과할 수 없는 경우 (이론적으로는 주어지지 않음)


# 입력 처리
T = int(input())

for tc in range(1, T + 1):
    D, W, K = map(int, input().split())  # 두께, 폭, 합격기준
    film = [list(map(int, input().split())) for _ in range(D)]  # 필름 정보

    # BFS를 통해 최소 약품 투입 횟수 계산
    result = BFS(film)

    # 출력
    print(f'#{tc} {result}')
