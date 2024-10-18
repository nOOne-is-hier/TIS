import sys
sys.stdin = open('input.txt')
import itertools


def calculate_vector_sum(coordinates, selected):
    vector_x, vector_y = 0, 0
    n = len(coordinates)

    for i in range(n):
        if i in selected:
            vector_x += coordinates[i][0]
            vector_y += coordinates[i][1]
        else:
            vector_x -= coordinates[i][0]
            vector_y -= coordinates[i][1]
    print(vector_x ** 2 + vector_y ** 2)
    print(selected)

    return vector_x ** 2 + vector_y ** 2


def find_min_vector_sum(coordinates):
    N = len(coordinates)
    min_sum = float('inf')

    # N개의 지렁이 중에서 N//2개를 선택하여 combination 생성
    print(tuple(itertools.combinations(range(N), N // 2)))
    for selected in itertools.combinations(range(N), N // 2):
        current_sum = calculate_vector_sum(coordinates, selected)
        min_sum = min(min_sum, current_sum)

    return min_sum


# Input handling
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    coordinates = [tuple(map(int, input().split())) for _ in range(N)]

    min_vector_sum = find_min_vector_sum(coordinates)
    print(f'#{t} {min_vector_sum}')
