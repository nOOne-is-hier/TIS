import sys
sys.stdin = open('input.txt')


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


# 필름의 행에 약품을 투입하는 함수 (약품 투입 후 상태 복원)
def inject_and_revert(row, chemical_type, state, original_row):
    # 필름의 해당 행을 약품으로 처리한 후 복구하는 방식
    for c in range(W):
        state[row][c] = chemical_type
    yield  # 처리 후 다음 상태로 진행 (yield로 상태 유지)
    for c in range(W):
        state[row][c] = original_row[c]  # 원래 상태로 복구


# DFS 탐색을 통해 최소 약품 투입 횟수 찾기
def DFS(state, depth, max_depth):
    if is_qualified(state):
        return depth

    if depth >= max_depth:
        return float('inf')

    min_depth = float('inf')

    for row in range(D):
        # 현재 상태 백업
        original_row = state[row][:]

        # 약품 A 투입
        for c in range(W):
            state[row][c] = 0
        min_depth = min(min_depth, DFS(state, depth + 1, max_depth))

        # 상태 복구
        state[row] = original_row[:]

        # 약품 B 투입
        for c in range(W):
            state[row][c] = 1
        min_depth = min(min_depth, DFS(state, depth + 1, max_depth))

        # 상태 복구
        state[row] = original_row[:]

    return min_depth


# 입력 처리
T = int(input())

for tc in range(1, T + 1):
    D, W, K = map(int, input().split())  # 두께, 폭, 합격기준
    film = [list(map(int, input().split())) for _ in range(D)]  # 필름 정보

    # 투입 횟수 0부터 차례대로 시도
    min_chemicals = 0
    while True:
        result = DFS(film, 0, min_chemicals)
        if result != float('inf'):
            break
        min_chemicals += 1

    # 출력
    print(f'#{tc} {min_chemicals}')
