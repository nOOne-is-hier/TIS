import sys
sys.stdin = open('input.txt')


def find_palindrome(line):
    for length in range(100, 0, -1):
        num_subset = 100 - length + 1
        for idx in range(num_subset):
            left = 0 + idx + 1
            right = left + length
            if line[left:right] == line[left:right][::-1]:
                return length


for _ in range(10):
    tc = int(input())
    array = [list(map(str, input())) for _ in range(100)]

    len_palindrome_list = {find_palindrome(row) for row in array} | {find_palindrome(column) for column in zip(*array)}

    print(f'#{tc}', max(len_palindrome_list))