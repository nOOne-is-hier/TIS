import sys
sys.stdin = open('input.txt')
import heapq
from collections import deque

Q = int(input())
orders = deque(map(int, input().split()))

ugly_numbers = set()
order_of_numbers = {}

for x in range(30):
    for y in range(20):
        for z in  range(15):
            ugly_numbers.add(2 ** x * 3 ** y * 5 ** z)

# 힙 변환
ugly_numbers = list(ugly_numbers)
heapq.heapify(ugly_numbers)

current = 0
while current != 1500:
    current += 1
    order_of_numbers[current]=heapq.heappop(ugly_numbers)
# print(order_of_numbers)

while orders:
    print(order_of_numbers[orders.popleft()], end=' ')

