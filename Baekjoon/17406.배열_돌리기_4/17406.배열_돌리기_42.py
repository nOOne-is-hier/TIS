import sys
from itertools import permutations
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

# 입력 받기
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
calculations = [tuple(map(int, input().split())) for _ in range(K)]


# 회전 연산 함수
def rotate(array, r, c, s):
    r, c = r - 1, c - 1  # 인덱스를 0부터 시작하도록 조정
    for i in range(1, s + 1):
        top, left, bottom, right = r - i, c - i, r + i, c + i

        # 바깥 테두리를 deque로 처리
        temp = deque()

        # 윗변 (왼쪽 → 오른쪽)
        for j in range(left, right):
            temp.append(array[top][j])
        # 오른쪽 변 (위 → 아래)
        for j in range(top, bottom):
            temp.append(array[j][right])
        # 아랫변 (오른쪽 → 왼쪽)
        for j in range(right, left, -1):
            temp.append(array[bottom][j])
        # 왼쪽 변 (아래 → 위)
        for j in range(bottom, top, -1):
            temp.append(array[j][left])

        # 시계 방향으로 한 칸 회전
        temp.rotate(1)

        # 값 다시 채우기
        # 윗변 (왼쪽 → 오른쪽)
        for j in range(left, right):
            array[top][j] = temp.popleft()
        # 오른쪽 변 (위 → 아래)
        for j in range(top, bottom):
            array[j][right] = temp.popleft()
        # 아랫변 (오른쪽 → 왼쪽)
        for j in range(right, left, -1):
            array[bottom][j] = temp.popleft()
        # 왼쪽 변 (아래 → 위)
        for j in range(bottom, top, -1):
            array[j][left] = temp.popleft()


# 모든 회전 연산 순서에 대해 배열 A의 최솟값 찾기
tmp_min = 5000
for perm in permutations(calculations):
    new_grid = [row[:] for row in grid]  # 초기 배열 복사
    for r, c, s in perm:
        rotate(new_grid, r, c, s)
    tmp_min = min(tmp_min, min(sum(row) for row in new_grid))

print(tmp_min)
