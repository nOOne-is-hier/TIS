# pypy 111,056KB 168ms
# python 34,972KB 940ms
import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())
screening_table = [0] * N
for idx in range(N):
    screening_table[idx] = int(input())

left = 1
right = max(screening_table) * M

while left <= right:
    mid = (left + right) >> 1
    total_passed = 0

    for table in screening_table:
        total_passed += mid // table
        if total_passed >= M:
            break

    if total_passed >= M:
        right = mid - 1
    else:
        left = mid + 1

print(left)