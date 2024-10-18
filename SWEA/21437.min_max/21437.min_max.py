import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    max_difference = max_num - numbers[0]
    for num in numbers:
        if max_num - num > max_difference:
            max_difference = max_num - num

    print(f'#{tc}', max_difference)