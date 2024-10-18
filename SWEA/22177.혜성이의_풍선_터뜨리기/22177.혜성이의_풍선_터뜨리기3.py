import sys

sys.stdin = open('input.txt')


def solve(state, N, balloons, memo, trace):
    # 모든 풍선을 터뜨린 상태이면 종료
    if state == (1 << N) - 1:
        return 0

    # 이미 계산한 상태이면 메모된 값 반환
    if memo[state] != -1:
        return memo[state]

    max_score = 0
    best_choice = -1  # 풍선을 터뜨린 위치 저장

    for current in range(N):
        if state & (1 << current):  # 이미 터뜨린 풍선은 스킵
            continue

        # 현재 풍선을 터뜨리는 작업 수행
        left = 1
        right = 1
        is_left = False
        is_right = False

        # 오른쪽 탐색
        r = current + 1
        while r < N:
            if state & (1 << r):
                r += 1
                continue
            else:
                right = balloons[r]
                is_right = True
                break

        # 왼쪽 탐색
        l = current - 1
        while l >= 0:
            if state & (1 << l):
                l -= 1
                continue
            else:
                left = balloons[l]
                is_left = True
                break

        # 점수 계산
        if is_left and is_right:
            current_score = left * right
        elif is_left:
            current_score = left
        elif is_right:
            current_score = right
        else:
            current_score = balloons[current]

        # 새로운 상태에서 재귀 호출 및 최대 점수 갱신
        new_state = state | (1 << current)
        new_score = current_score + solve(new_state, N, balloons, memo, trace)

        if new_score > max_score:
            max_score = new_score
            best_choice = current  # 현재 터뜨린 풍선을 기록

    # 현재 상태의 최적값을 메모
    memo[state] = max_score
    trace[state] = best_choice  # 최적의 선택을 추적
    return max_score


# 풍선을 터뜨리는 순서 추적 함수
def find_sequence(trace, N):
    state = 0
    sequence = []
    while state != (1 << N) - 1:
        current = trace[state]
        sequence.append(current + 1)  # 풍선 번호를 1부터 시작한다고 가정
        state |= (1 << current)
    return sequence


# 입력 받기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    balloons = list(map(int, input().split()))

    # 메모이제이션 테이블 (-1로 초기화)
    memo = [-1] * (1 << N)
    trace = [-1] * (1 << N)  # 추적용 배열

    # 최종 결과 계산
    result = solve(0, N, balloons, memo, trace)

    # 풍선을 터뜨리는 순서 추적
    sequence = find_sequence(trace, N)

    # 결과 출력
    print(f'#{tc} {result}')
    print("Balloon bursting order:", sequence)
