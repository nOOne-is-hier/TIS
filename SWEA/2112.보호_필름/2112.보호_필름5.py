import sys
sys.stdin = open('input.txt')
from itertools import combinations, product

# 성능 검사가 통과하는지 확인하는 함수
def is_passed(array):
    for i in range(W):
        a, b = 0, 0
        for j in range(D):
            if array[j][i] == 0:
                a += 1
                b = 0
            else:
                a = 0
                b += 1
            if a >= K or b >= K:
                break
        else:
            return False
    return True

# 백트래킹으로 최소 약품 투입 횟수를 찾는 함수
def backtracking():
    # 초기 상태가 통과하는지 먼저 확인
    if is_passed(arr):
        return 0

    temp = [arr[i][:] for i in range(D)]  # 원본 배열 저장
    ans = D  # 최대 투입 가능 횟수는 D

    # 1부터 D개까지의 조합을 탐색
    for i in range(1, D + 1):
        # 약품 투입 횟수가 현재 최적값보다 많으면 종료
        if i >= ans:
            break

        # i개의 행에 약품을 투입하는 모든 조합
        for row_comb in combinations(range(D), i):
            # A 또는 B 약품을 투입하는 모든 경우
            for trials in product([0, 1], repeat=i):
                for idx, trial in zip(row_comb, trials):
                    arr[idx] = [trial] * W  # 해당 행에 약품 A(0) 또는 B(1) 투입

                # 성능 검사를 통과하면 최소 횟수 갱신
                if is_passed(arr):
                    ans = min(i, ans)
                    break

                # 복구: 원래 상태로 복구
                for idx in row_comb:
                    arr[idx] = temp[idx]

            # 이미 더 작은 약품 투입 횟수로 통과하면 탐색 중단
            if ans == i:
                return ans

    return ans

# 입력 처리
T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]

    # 백트래킹을 통해 최소 약품 투입 횟수 계산
    result = backtracking()

    # 결과 출력
    print(f'#{tc} {result}')
