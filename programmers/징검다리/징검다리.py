import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')


def solution(distance, rocks, n):
    num_of_rocks = len(rocks)
    distance_changes = []
    sorted_rocks = [0] + sorted(rocks) + [distance]
    for idx in range(1, num_of_rocks + 2):
        current_distance = sorted_rocks[idx] - sorted_rocks[idx - 1]
        heappush(distance_changes, current_distance)

    for _ in range(num_of_rocks - n + 1):
        smallest_distance = heappop(distance_changes)

    return smallest_distance

print(solution(25, [2, 14, 11, 21, 17], 2))
