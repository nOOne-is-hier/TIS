import sys
sys.stdin = open('input.txt')

from collections import deque

for _ in range(int(input())):
    N, target = map(int, input().split())

    before_ordered = deque(enumerate(map(int, input().split())))
    print_que = [0] * N

    step = 0
    while before_ordered:
        to_next = False
        step += 1
        current = before_ordered.popleft()

        for order in before_ordered:
            if current[1] < order[1]:
                before_ordered.append(current)
                step -= 1
                to_next = True
                break

        if to_next:
            continue

        if current[0] == target:
            print(step)
            break