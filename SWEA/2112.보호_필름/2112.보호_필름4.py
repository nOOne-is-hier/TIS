import sys
sys.stdin = open('input.txt')

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

# DP 테이블
dp = {}

# DFS + DP를 통해 최소 약품 투입 횟수 찾기 (비트마스크)
def DFS(state_bits, depth, max_depth):
    # 필름이 이미 성능 기준을 충족하는지 확인
    if is_qualified(state_bits):
        return depth

    # 깊이가 최대 투입 횟수를 초과하면 더 이상 탐색하지 않음
    if depth >= max_depth:
        return D + 1  # 무한대 대신 최대 D + 1로 설정

    # 현재 상태를 DP 테이블에서 확인 (메모이제이션)
    state_tuple = tuple(state_bits)
    if state_tuple in dp and dp[state_tuple] <= depth:
        return D + 1  # 무한대 대신 최대 D + 1로 설정

    # DP 테이블 업데이트
    dp[state_tuple] = depth

    min_depth = D + 1  # 무한대 대신 최대 D + 1로 설정

    # 약품 A(0)를 먼저 투입해보고 성능이 좋은 쪽을 우선 탐색
    for row in range(D):
        original_row = state_bits[row]

        # 약품 A(0) 투입
        state_bits[row] = 0  # 모든 셀을 0으로 변경 (약품 A)
        result_A = DFS(state_bits, depth + 1, max_depth)
        min_depth = min(min_depth, result_A)

        # 약품 B(1) 투입
        state_bits[row] = (1 << W) - 1  # 모든 셀을 1로 변경 (약품 B)
        result_B = DFS(state_bits, depth + 1, max_depth)
        min_depth = min(min_depth, result_B)

        # 원래 상태 복구
        state_bits[row] = original_row

        # 가지치기 - 현재 최소 깊이보다 큰 경우 더 이상 탐색하지 않음
        if min_depth <= depth + 1:
            break

    return min_depth


# 입력 처리
T = int(input())
results = []  # 모든 결과를 모아서 한 번에 출력

for tc in range(1, T + 1):
    D, W, K = map(int, input().split())  # 두께, 폭, 합격기준
    film = [int(''.join(map(str, input().split())), 2) for _ in range(D)]  # 필름을 비트마스크로 변환

    # 투입 횟수 0부터 차례대로 시도
    min_chemicals = 0
    while True:
        dp.clear()  # DP 테이블 초기화
        result = DFS(film, 0, min_chemicals)
        if result != D + 1:  # 무한대 대신 D + 1로 체크
            break
        min_chemicals += 1

    # 결과를 저장
    results.append(f'#{tc} {min_chemicals}')

# 한 번에 출력
print("\n".join(results))
