import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    ordinal_num = 0
    counted_numbers = set()

    while len(counted_numbers) != 10:
        ordinal_num += 1
        number = N * ordinal_num

        for num in str(number):
            counted_numbers.add(num)

    print(f'#{tc} {number}')