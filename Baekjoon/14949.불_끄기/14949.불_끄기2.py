# python 31,120KB 36ms
import sys

sys.stdin = open('input.txt')


# 입력 처리: '#' -> 0, 'O' -> 1
def input_lights():
    lights = []
    for _ in range(10):
        lights.append([0 if light == '#' else 1 for light in input().strip()])
    return lights


# 가우스 소거법을 사용하여 문제를 해결하는 함수
def gaussian_elimination(matrix, b):
    # 가우스 소거법을 통해 상삼각 행렬로 변환
    for i in range(100):
        if matrix[i][i] == 0:
            for j in range(i + 1, 100):
                if matrix[j][i] == 1:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    b[i], b[j] = b[j], b[i]
                    break
        if matrix[i][i] == 0:
            continue
        for j in range(i + 1, 100):
            if matrix[j][i] == 1:
                for k in range(i, 100):
                    matrix[j][k] ^= matrix[i][k]
                b[j] ^= b[i]

    # 뒤에서부터 해를 구해가는 방식
    x = [0] * 100
    for i in range(99, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, 100):
            x[i] ^= matrix[i][j] * x[j]

    return x


def solve_lights_out_with_gaussian():
    lights = input_lights()
    matrix = [[0] * 100 for _ in range(100)]
    b = [0] * 100

    # 버튼을 누를 때 영향 받는 칸을 표시하는 100x100 행렬 구성
    for r in range(10):
        for c in range(10):
            idx = r * 10 + c
            matrix[idx][idx] = 1
            if r > 0: matrix[idx][(r - 1) * 10 + c] = 1  # 위쪽
            if r < 9: matrix[idx][(r + 1) * 10 + c] = 1  # 아래쪽
            if c > 0: matrix[idx][r * 10 + (c - 1)] = 1  # 왼쪽
            if c < 9: matrix[idx][r * 10 + (c + 1)] = 1  # 오른쪽
            b[idx] = lights[r][c]  # 목표 상태 (켜져 있으면 1)

    # 가우스 소거법으로 해 찾기
    x = gaussian_elimination(matrix, b)

    # 버튼 누름 횟수 계산
    return sum(x)


# 실행
print(solve_lights_out_with_gaussian())
