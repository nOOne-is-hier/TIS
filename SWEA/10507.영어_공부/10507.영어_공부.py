import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, P = map(int, input().split())

    days_table = [[True, 1] for _ in range(1000001)]
    pointer_with_index = {}

    for studied_day in map(int, input().split()):
        days_table[studied_day] = False

    curser = 0
    not_studied_straight = 0
    adjacent_study_days = 0
    last_not_studied_day = None
    max_value_when_p_is_1 = 0
    while curser < 1000001:
        if days_table[curser]:
            days_table[curser][0] = not_studied_straight
            days_table[curser][1] = adjacent_study_days
            if last_not_studied_day is not None:
                days_table[last_not_studied_day][1] += adjacent_study_days
                max_value_when_p_is_1 = max(max_value_when_p_is_1, days_table[last_not_studied_day][1])
            adjacent_study_days = 0
            last_not_studied_day = curser
            pointer_with_index[not_studied_straight] = curser
            not_studied_straight += 1
        else:
            adjacent_study_days += 1
        curser += 1
    if last_not_studied_day is not None:
        days_table[last_not_studied_day][1] += adjacent_study_days
        max_value_when_p_is_1 = max(max_value_when_p_is_1, days_table[last_not_studied_day][1])

    if P == 1:
        print(f'#{tc}', max_value_when_p_is_1 + 1)
    else:
        left = 0
        right = left + P
        result = 1
        while right < not_studied_straight:
            tmp_max = pointer_with_index[right] - pointer_with_index[left]
            result = max(result, tmp_max)
            left += 1
            right += 1

        print(f'#{tc}', result)
