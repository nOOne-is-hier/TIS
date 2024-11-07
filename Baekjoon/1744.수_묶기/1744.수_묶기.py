import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')

N = int(input())

pluses = []; size_of_pluses = 0
minuses = []; size_of_minuses = 0
num_of_zero = 0
num_of_one = 0
for _ in range(N):
    num = int(input())
    if num > 1:
        heappush(pluses, -num)
        size_of_pluses += 1
    elif num < 0:
        heappush(minuses, num)
        size_of_minuses += 1
    elif num == 0:
        num_of_zero += 1
    else:
        num_of_one += 1

result = num_of_one
for cnt in range(size_of_minuses // 2):
    result = result + heappop(minuses) * heappop(minuses)
if minuses and not num_of_zero:
    result += heappop(minuses)
for cnt in range(size_of_pluses // 2):
    result = result + heappop(pluses) * heappop(pluses)
if pluses:
    result += -heappop(pluses)
print(result)