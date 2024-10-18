import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    # N = 학생의 수, M = 문제의 수
    N, M = list(map(int, input().split()))
    # 답안지, 구간합 표현을 위해 앞에 0 추가
    answer_sheet = [0] + list(map(int, input().split()))
    # 최고 점수, 최저 점수
    max_sum_score = 0
    min_sum_score = 56

    # 채점 시작
    for _ in range(N):
        response_sheet = [0] + list(map(int, input().split()))

        scores = [0] * (M+1)

        # 성적표 구하기
        for number in range(1, M + 1):
            if response_sheet[number] == answer_sheet[number]:
                scores[number] = scores[number-1] + 1

        if sum(scores) > max_sum_score:
            max_sum_score = sum(scores)

        if sum(scores) < min_sum_score:
            min_sum_score = sum(scores)

    print(f'#{tc} {max_sum_score-min_sum_score}')
