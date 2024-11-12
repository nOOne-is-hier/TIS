import os
import array
from itertools import permutations


def rotate_layer(a, r, c, s, n, m):
    for d in range(1, s + 1):
        top, left, bottom, right = r - d, c - d, r + d, c + d
        prev = a[top * m + left]

        # 윗변 (왼쪽 → 오른쪽)
        for idx in range(left + 1, right + 1):
            a[top * m + idx], prev = prev, a[top * m + idx]
        # 오른쪽 변 (위 → 아래)
        for idx in range(top + 1, bottom + 1):
            a[idx * m + right], prev = prev, a[idx * m + right]
        # 아랫변 (오른쪽 → 왼쪽)
        for idx in range(right - 1, left - 1, -1):
            a[bottom * m + idx], prev = prev, a[bottom * m + idx]
        # 왼쪽 변 (아래 → 위)
        for idx in range(bottom - 1, top - 1, -1):
            a[idx * m + left], prev = prev, a[idx * m + left]


def main():
    # os.read를 사용하여 입력을 읽기
    input_data = os.read(0, os.fstat(0).st_size).decode().splitlines()

    # 입력 처리
    N, M, K = map(int, input_data[0].split())
    grid = array.array('i', [0] * (N * M))

    # 2차원 배열을 1차원 배열로 변환하여 저장
    index = 0
    for i in range(1, N + 1):
        values = map(int, input_data[i].split())
        for value in values:
            grid[index] = value
            index += 1

    calculations = [tuple(map(int, input_data[i + N + 1].split())) for i in range(K)]
    tmp_min = float('inf')  # 초기값을 무한대로 설정

    # 모든 회전 연산 순서에 대해 배열의 최솟값 찾기
    for perm in permutations(calculations):
        new_state = array.array('i', grid)  # 초기 배열 복사
        for p in perm:
            rotate_layer(new_state, p[0] - 1, p[1] - 1, p[2], N, M)

        # 현재 순열의 결과로 최소 행의 합 계산
        current_min = float('inf')
        for i in range(N):
            row_sum = sum(new_state[i * M:(i + 1) * M])
            current_min = min(current_min, row_sum)

        tmp_min = min(tmp_min, current_min)

    # 결과 출력
    print(tmp_min)


if __name__ == "__main__":
    main()
