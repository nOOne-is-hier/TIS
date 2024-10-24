# pypy 111,056KB 172ms
# python 34,972KB 868ms
import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())
screening_table = [0] * N
for idx in range(N):
    screening_table[idx] = int(input())

left = 1
right = 10 ** 18

while left <= right:
    mid = (left + right) // 2
    total_passed = 0

    for table in screening_table:
        total_passed += mid // table
        if total_passed >= M:
            break

    if total_passed >= M:
        right = mid - 1
        min_time = mid
    else:
        left = mid + 1

print(min_time)