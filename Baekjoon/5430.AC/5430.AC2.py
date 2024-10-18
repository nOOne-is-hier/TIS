import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

from collections import deque

for tc in range(int(input())):
    p = input().split()
    n = int(input())
    input_string = input().strip('[]\n')

    if not input_string:
        array = deque()
    else:
        array = deque(input_string.split(','))
    no_Error = True
    direction_of_array = True

    for func in p[0]:
        if func == 'D':
            if not array:
                print('error')
                no_Error = False
                break

            n -= 1
            if direction_of_array:
                array.popleft()
            else:
                array.pop()

        else:
            if direction_of_array:
                direction_of_array = False
            else:
                direction_of_array = True

    if no_Error:
        if not direction_of_array:
            new_array = []
            for _ in range(n):
                new_array.append(array.pop())
            print('[', end='')
            print(','.join(new_array), end='')
            print(']')

        else:
            print('[', end='')
            print(','.join(list(array)), end='')
            print(']')

