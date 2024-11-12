import sys
from itertools import permutations

def rotate_layer(array, r, c, s):
    for dis in range(1, s + 1):
        top, left, bottom, right = r - dis, c - dis, r + dis, c + dis
        prev = array[top][left]

        # 윗변 (왼쪽 → 오른쪽)
        for idx in range(left + 1, right + 1):
            array[top][idx], prev = prev, array[top][idx]
        # 오른쪽 변 (위 → 아래)
        for idx in range(top + 1, bottom + 1):
            array[idx][right], prev = prev, array[idx][right]
        # 아랫변 (오른쪽 → 왼쪽)
        for idx in range(right - 1, left - 1, -1):
            array[bottom][idx], prev = prev, array[bottom][idx]
        # 왼쪽 변 (아래 → 위)
        for idx in range(bottom - 1, top - 1, -1):
            array[idx][left], prev = prev, array[idx][left]

def main():
    sys.stdin = open('input.txt')
    input = sys.stdin.readline

    # 입력 처리
    N, _, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    calculations = tuple(tuple(map(int, input().split())) for _ in range(K))
    tmp_min = 5000  # 초기값을 무한대로 설정

    # 모든 회전 연산 순서에 대해 배열의 최솟값 찾기
    for perm in permutations(calculations):
        new_state = [line[:] for line in grid]  # 초기 배열 복사
        for p in perm:
            rotate_layer(new_state, p[0] - 1, p[1] - 1, p[2])

        # 현재 순열의 결과로 최소 행의 합 계산
        current_min = min(sum(row) for row in new_state)
        tmp_min = min(tmp_min, current_min)

    # 결과 출력
    print(tmp_min)

main()
