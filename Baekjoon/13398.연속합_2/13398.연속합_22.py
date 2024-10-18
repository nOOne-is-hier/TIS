import sys

sys.stdin = open('input.txt')

# 입력 처리
N = int(input())
array = list(map(int, input().split()))

# DP 테이블 초기화
tmp_max_table = [[0, 0] for _ in range(N)]  # 독립적인 리스트로 초기화
tmp_max_table[0] = [array[0], 0]
current_max = tmp_max_table[0][0]

# 탐색 시작 (기본 카데인 알고리즘 적용)
for idx in range(1, N):
    if tmp_max_table[idx - 1][0] + array[idx] > array[idx]:
        tmp_max_table[idx] = [tmp_max_table[idx - 1][0] + array[idx], tmp_max_table[idx - 1][1]]
    else:
        tmp_max_table[idx] = [array[idx], idx - 1]  # 직전 인덱스에 대해 -1 조정

    # 현재까지의 최대 구간합 갱신
    current_max = max(tmp_max_table[idx][0], current_max)

# 음수를 제외하는 백트래킹 로직
for cursor in range(N):
    if array[cursor] < 0:  # 음수를 만난 경우
        for idx in range(cursor, N):
            start_idx = tmp_max_table[idx][1]  # dp 테이블에서 시작 인덱스 가져옴

            # 백트래킹 중 start_idx에 따른 처리
            if start_idx > cursor:
                break

            if start_idx == cursor:  # 음수를 만났을 때
                if cursor > 0:
                    tmp_max = tmp_max_table[idx][0] + tmp_max_table[cursor - 1][0]
                else:  # 음수의 인덱스가 0일 때
                    tmp_max = tmp_max_table[idx][0]
            elif start_idx + 1 == cursor:
                tmp_max = tmp_max_table[idx][0]

            else:  # 음수를 제외하는 경우
                tmp_max = tmp_max_table[idx][0] - array[cursor]

            # 최대 구간합 갱신
            current_max = max(tmp_max, current_max)

# 최종 결과 출력
print(current_max)
