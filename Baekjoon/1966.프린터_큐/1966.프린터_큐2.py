import sys
sys.stdin = open('input.txt')

from collections import deque

for _ in range(int(input())):
    N, target = map(int, input().split())
    queue = deque(enumerate(map(int, input().split())))
    step = 0

    while queue:
        current = queue.popleft()

        if any(current[1] < other[1] for other in queue):
            queue.append(current)
        else:
            step += 1
            if current[0] == target:
                print(step)
                break
