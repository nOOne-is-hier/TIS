import sys

# 입력 파일을 표준 입력으로 설정
sys.stdin = open('input.txt')

# 주어진 구간 내에서 학습하지 않은 날의 수를 계산하는 함수
def count_not_studied_day(start, end):
    return not_studied_straight[end] - (not_studied_straight[start - 1] if start > 0 else 0)

# 특정 길이(mid)가 가능한지 확인하는 함수 (학습하지 않은 날의 수가 P 이하인지 확인)
def is_possible_length(mid, P):
    for start in range(1000001 - mid + 1):
        end = start + mid - 1

        # start부터 end까지의 학습하지 않은 날의 수를 계산
        count_not_studied = count_not_studied_day(start, end)

        # 학습하지 않은 날의 수가 P 이하라면 해당 길이로 가능한 것으로 판단
        if count_not_studied <= P:
            return True

    return False

# 테스트 케이스 개수 입력
T = int(input())

# 각 테스트 케이스 처리
for tc in range(1, T + 1):
    # N: 총 학습일 수, P: 불연속적인 최대 학습 기간
    N, P = map(int, input().split())

    # 모든 날을 학습 가능한 상태로 초기화
    days_table = [True] * 1000001

    # 학습한 날을 입력받아 그 날들을 학습하지 않은 날로 설정
    for studied_day in map(int, input().split()):
        days_table[studied_day] = False

    # 학습하지 않은 날의 누적 합 배열을 생성
    not_studied_straight = [0] * 1000001
    for day in range(1, 1000001):
        not_studied_straight[day] = not_studied_straight[day - 1] + (1 if days_table[day] else 0)

    # 이분 탐색을 통해 가능한 최대 연속 학습 기간을 찾음
    left, right = 0, 1000001
    result = -1
    while left <= right:
        mid = (left + right) // 2

        # 현재 길이(mid)가 가능한지 확인
        if is_possible_length(mid, P):
            result = mid
            left = mid + 1  # 가능한 경우 더 큰 길이를 찾기 위해 left 증가
        else:
            right = mid - 1  # 불가능한 경우 더 작은 길이를 찾기 위해 right 감소

    # 결과 출력
    print(f'#{tc}', result)
