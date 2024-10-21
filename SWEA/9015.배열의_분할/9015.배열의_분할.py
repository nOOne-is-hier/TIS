# pypy 89,924KB 552ms
import sys

# 입력 파일을 표준 입력으로 설정
sys.stdin = open('input.txt')

# 테스트 케이스 개수 입력
T = int(input())

# 각 테스트 케이스 처리
for tc in range(1, T + 1):
    # 배열의 크기 입력
    N = int(input())
    # 배열 요소 입력
    numbers = list(map(int, input().split()))

    # 최소 분할할 부분 배열의 개수 초기화 (최소 1개는 필요)
    num_of_arrays = 1
    # 현재 기울기를 저장할 변수 초기화 (아직 결정되지 않음)
    current_slope = None

    # 배열의 각 요소를 순회하며 기울기 변화 확인
    for idx in range(1, N):
        # 기울기가 아직 정해지지 않은 경우 초기 기울기를 설정
        if current_slope is None:
            if numbers[idx - 1] < numbers[idx]:
                current_slope = 1  # 오름차순
            elif numbers[idx - 1] > numbers[idx]:
                current_slope = -1  # 내림차순
            elif numbers[idx - 1] == numbers[idx]:
                current_slope = None  # 같은 경우 기울기 설정 없음
            continue

        # 같은 값일 경우 현재 기울기는 유지 (아무 것도 하지 않음)
        if numbers[idx - 1] == numbers[idx]:
            continue
        # 오름차순으로 전환되는 경우 새로운 부분 배열 시작
        elif numbers[idx - 1] < numbers[idx] and current_slope != 1:
            num_of_arrays += 1
            current_slope = None
        # 내림차순으로 전환되는 경우 새로운 부분 배열 시작
        elif numbers[idx - 1] > numbers[idx] and current_slope != -1:
            num_of_arrays += 1
            current_slope = None

    # 결과 출력
    print(f'#{tc}', num_of_arrays)
