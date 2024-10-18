import sys

sys.stdin = open('input.txt')

N = int(input())

orders = [list(input().split()) for _ in range(N)]

deq = [0] * N
front = rear = -1

for order in orders:
    if order[0] == 'enqueue':
        rear += 1
        deq[rear] = order[1]
    elif order[0] == 'front':
        print(deq[front+1])
    elif order[0] == 'rear':
        print(deq[rear])
    elif order[0] == 'dequeue':
        front += 1
        print(deq[front])
        deq[front] = 0
    elif order[0] == 'isEmpty':
        if front == rear:
            print(1)
        else:
            print(-1)
    elif order[0] == 'size':
        print(rear-front)