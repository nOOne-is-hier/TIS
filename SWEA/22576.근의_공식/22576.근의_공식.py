import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    modulus = 10 ** 9
    left = 0
    right = 10 ** 9
    result = -1
    while left <= right:
        mid = (left + right) // 2
        mod_result = (mid ** 2 * A + mid * B + C) % modulus
        if mod_result == 0:
            result = mid
            break
        else:
            if mod_result <= modulus // 2:
                right = mid - 1
            else:
                left = mid + 1

    print(result)
