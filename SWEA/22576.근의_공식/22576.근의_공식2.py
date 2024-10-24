import sys

sys.stdin = open('input.txt')

T = int(input())
modulus = 10 ** 9

# 분할 정복을 위한 재귀 함수 정의
def divide_and_conquer(left, right, A, B, C):
    if left > right:
        return -1

    # 중앙값 계산
    mid = (left + right) // 2

    # f(x) 계산
    f_mid = A * mid ** 2 + B * mid + C
    mod_result = f_mid % modulus

    # 나머지가 0인 경우 찾기
    if mod_result == 0:
        return mid

    # 왼쪽 구간 탐색
    left_result = divide_and_conquer(left, mid - 1, A, B, C)
    if left_result != -1:
        return left_result

    # 오른쪽 구간 탐색
    return divide_and_conquer(mid + 1, right, A, B, C)

# 테스트 케이스 실행
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    left = 0
    right = 10 ** 9
    result = divide_and_conquer(left, right, A, B, C)
    print(result)
