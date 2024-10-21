import sys

# 입력 파일을 표준 입력으로 설정
sys.stdin = open('input.txt')

# 테스트 케이스 개수 입력
T = int(input())

# 각 테스트 케이스 처리
for tc in range(1, T + 1):
    # N: 총 학습일 수, P: 불연속적인 최대 학습 기간
    N, P = map(int, input().split())

    # 모든 날을 학습 가능한 상태로 초기화 [True, 1]로 설정
    days_table = [[True, 1] for _ in range(1000001)]
    # 불연속적으로 학습하지 않은 날에 대한 포인터와 인덱스를 저장
    pointer_with_index = {}

    # 학습한 날을 입력받아 그 날들을 학습하지 않은 날로 설정
    for studied_day in map(int, input().split()):
        days_table[studied_day] = False

    # 변수 초기화
    curser = 0  # 현재 커서 위치
    not_studied_straight = 0  # 연속해서 학습하지 않은 날의 수
    adjacent_study_days = 0  # 연속한 학습일의 수
    last_not_studied_day = None  # 마지막으로 학습하지 않은 날의 위치
    max_value_when_p_is_1 = 0  # P가 1일 때 최대 학습일 수

    # 모든 날을 순회하면서 처리
    while curser < 1000001:
        # 현재 날이 학습되지 않은 날일 경우
        if days_table[curser]:
            days_table[curser][0] = not_studied_straight  # 연속된 학습되지 않은 날의 수 기록
            days_table[curser][1] = adjacent_study_days  # 연속된 학습일 수 기록
            if last_not_studied_day is not None:
                days_table[last_not_studied_day][1] += adjacent_study_days  # 이전 학습되지 않은 날에 현재 연속된 학습일 추가
                max_value_when_p_is_1 = max(max_value_when_p_is_1, days_table[last_not_studied_day][1])  # 최대 학습일 계산
            # 연속 학습일 초기화
            adjacent_study_days = 0
            # 마지막 학습하지 않은 날 업데이트
            last_not_studied_day = curser
            # 포인터와 인덱스 저장
            pointer_with_index[not_studied_straight] = curser
            # 연속 학습하지 않은 날 증가
            not_studied_straight += 1
        else:
            # 현재 날이 학습일일 경우, 연속된 학습일 증가
            adjacent_study_days += 1
        # 커서를 다음 날로 이동
        curser += 1

    # 마지막 학습되지 않은 날에 대해 처리
    if last_not_studied_day is not None:
        days_table[last_not_studied_day][1] += adjacent_study_days
        max_value_when_p_is_1 = max(max_value_when_p_is_1, days_table[last_not_studied_day][1])

    # P가 1일 경우, 최대 연속 학습일 + 1 출력
    if P == 1:
        print(f'#{tc}', max_value_when_p_is_1 + 1)
    else:
        # P가 1보다 큰 경우 슬라이딩 윈도우 방식으로 처리
        left = 0
        right = left + P
        result = 1
        # 슬라이딩 윈도우를 사용해 최대 값을 찾음
        while right < not_studied_straight:
            tmp_max = pointer_with_index[right] - pointer_with_index[left]
            result = max(result, tmp_max)
            left += 1
            right += 1

        print(f'#{tc}', result)
