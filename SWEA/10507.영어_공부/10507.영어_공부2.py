import sys

sys.stdin = open('input.txt')


def count_not_studied_day(start, end):
    return not_studied_straight[end] - (not_studied_straight[start - 1] if start > 0 else 0)


def is_possible_length(mid, P):
    for start in range(1000001 - mid + 1):
        end = start + mid - 1

        count_not_studied = count_not_studied_day(start, end)

        if count_not_studied <= P:
            return True

    return False


T = int(input())

for tc in range(1, T + 1):
    N, P = map(int, input().split())

    days_table = [True] * 1000001

    for studied_day in map(int, input().split()):
        days_table[studied_day] = False

    not_studied_straight = [0] * 1000001
    for day in range(1, 1000001):
        not_studied_straight[day] = not_studied_straight[day - 1] + (1 if days_table[day] else 0)

    left, right = 0, 1000001
    result = -1
    while left <= right:
        mid = (left + right) // 2

        if is_possible_length(mid, P):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    print(f'#{tc}', result)