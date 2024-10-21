import sys

# 입력 파일을 표준 입력으로 설정
sys.stdin = open('input.txt')

# 테스트 케이스 개수 입력
T = int(input())
output = '#{} {}'

# 각 테스트 케이스 처리
for tc in range(1, T + 1):
    # N: 총 학습일 수, P: 불연속적인 최대 학습 기간
    N, P = map(int, input().split())
    studied_days = list(map(int, input().split()))

    result = -1
    start = 0

    # 투 포인터 (슬라이딩 윈도우) 사용하여 최대 연속 학습 가능 일 수 계산
    for end in range(N):
        # 현재 구간 내에서 불연속 학습일 수가 P를 초과하는 경우 시작점 이동
        while (studied_days[end] - studied_days[start] + 1) - (end - start + 1) > P:
            start += 1

        # 최대 학습 가능 일 수 갱신
        result = max(result, end - start + 1 + P)

    # 결과 출력
    print(output.format(tc, result))
