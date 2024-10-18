from collections import deque
import sys

sys.stdin = open('input.txt')

N = int(input())

orders = [list(input().split()) for _ in range(N)]

deq = deque()

for order in orders:
    if order[0] == 'enqueue':
        deq.append(order[1])
    elif order[0] == 'front':
        print(deq[0])
    elif order[0] == 'rear':
        print(deq[-1])
    elif order[0] == 'dequeue':
        print(deq.popleft())
    elif order[0] == 'isEmpty':
        if len(deq) != 0:
            print(-1)
        else:
            print(1)
    elif order[0] == 'size':
        print(len(deq))