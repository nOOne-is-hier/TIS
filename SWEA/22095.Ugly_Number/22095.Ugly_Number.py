import sys
sys.stdin = open('input.txt')
from collections import deque

Q = int(input())
orders = deque(map(int, input().split()))

order = 0
num = 0
while orders:
    current = orders.popleft()

    if current == 1:
        num += 1
        order += 1
        print(1, end=' ')
        continue

    while True:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            order += 1
            if current == order:
                print(num, end=' ')
                num += 1
                break
        num += 1

