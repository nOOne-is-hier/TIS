import sys

sys.stdin = open('input.txt')


def solution(distance, rocks, n):
    num_of_rocks = len(rocks)
    distance_changes = [0] * (num_of_rocks + 1)
    sorted_rocks = [0] + sorted(rocks) + [distance]
    for idx in range(1, num_of_rocks + 2):
        distance_changes[idx - 1] = sorted_rocks[idx] - sorted_rocks[idx - 1]
    start = 0
    for end in range(num_of_rocks + 1):

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))