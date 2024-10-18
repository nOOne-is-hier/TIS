import sys

sys.stdin = open('input.txt')

# 상태 업데이트 함수: 비트마스크 상태를 갱신하여 새로운 상태 반환
def update_state(state1, state2, state3, move):
    # state1, state2, state3를 각각 8비트로 관리
    combined = (state1 << 16) | (state2 << 8) | state3
    combined = ((combined << move) | (1 if move == 1 else 0)) & ((1 << 24) - 1)  # 24비트로 유지
    new_state1 = (combined >> 16) & 0xFF
    new_state2 = (combined >> 8) & 0xFF
    new_state3 = combined & 0xFF
    return new_state1, new_state2, new_state3

# 기본인자를 사용해서 함수를 여러 번 호출할 때 마다 각 변수들을 초기화할 수 있다
def findMaxScore(start=-1, last_step=2, state1=0, state2=0, state3=0, current_score=0, max_score=None):
    # 최종 결과 추적
    if max_score is None:
        max_score = [0]

    # 메모이제이션
    # 현재 위치와 비트마스크 상태를 결합해 고유한 키 생성
    current_key = (start, last_step, state1, state2, state3)

    # 가지치기 (이미 방문한 상태와 현재 점수를 비교)
    if current_key in memo:
        if memo[current_key] >= current_score:
            return

    # 고유한 상태 저장
    memo[current_key] = current_score

    # base condition: 마지막 계단에 도달했을 때
    if start == N - 1:
        max_score[0] = max(max_score[0], current_score)  # 마지막 계단의 점수 포함
        return

    # 한 칸을 뛰어서 왔다면, 두 칸만 뛸 수 있다. 단, 0번 인덱스는 예외
    if last_step == 1 and start != 0:
        if start + 2 < N:
            new_state1, new_state2, new_state3 = update_state(state1, state2, state3, 2)
            findMaxScore(start + 2, 2, new_state1, new_state2, new_state3, current_score + stairs[start + 2], max_score)

    # 두 칸을 뛰어서 왔다면, 한 칸이든 두 칸이든 뛸 수 있다. 단, 0번 인덱스는 예외
    elif last_step == 2 or start == 0:
        if start + 1 < N:
            new_state1, new_state2, new_state3 = update_state(state1, state2, state3, 1)
            findMaxScore(start + 1, 1, new_state1, new_state2, new_state3, current_score + stairs[start + 1], max_score)
        if start + 2 < N:
            new_state1, new_state2, new_state3 = update_state(state1, state2, state3, 2)
            findMaxScore(start + 2, 2, new_state1, new_state2, new_state3, current_score + stairs[start + 2], max_score)

    return

# 입력 처리
N = int(input())
stairs = [int(input()) for _ in range(N)]

# 상태를 저장하기 위한 메모이제이션 딕셔너리
memo = {}

# 결과 계산
max_score = [0]
findMaxScore(max_score=max_score)
print(max_score[0])
