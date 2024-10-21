# pypy 94,780KB 514ms
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

    # 변화량 배열을 구해 부호만 남김 (증가: 1, 감소: -1, 동일: 0)
    diffs = []
    for idx in range(1, N):
        if numbers[idx] > numbers[idx - 1]:
            diffs.append(1)  # 증가
        elif numbers[idx] < numbers[idx - 1]:
            diffs.append(-1)  # 감소
        else:
            diffs.append(0)  # 동일

    # 최소 분할할 부분 배열의 개수 초기화
    num_of_arrays = 1
    # 현재 기울기를 저장할 변수 초기화 (아직 결정되지 않음)
    current_slope = 0

    # 변화량 배열을 순회하며 기울기 변화 확인
    for diff in diffs:
        if diff == 0:
            continue  # 동일한 경우는 기울기 유지

        if current_slope == 0:
            current_slope = diff

        if current_slope != diff:
            num_of_arrays += 1
            current_slope = 0

    # 결과 출력
    print(f'#{tc}', num_of_arrays)
