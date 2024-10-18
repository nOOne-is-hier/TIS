import sys

sys.stdin = open('input.txt')


def Combinations(n, start=0, case=None, is_visited=None):
    if case is None:
        case = []
    if is_visited is None:
        is_visited = [0] * n

    if len(case) == n // 2:
        combinations.append(case[:])
        return

    for num in range(start, n):
        if not is_visited[num]:
            is_visited[num] = 1
            case.append(num)
            Combinations(n, num + 1, case, is_visited)
            case.pop()
            is_visited[num] = 0

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

    return vector_x ** 2 + vector_y ** 2


def find_min_vector_sum(coordinates):
    N = len(coordinates)
    min_sum = float('inf')

    # N개의 지렁이 중에서 N//2개를 선택하여 combination 생성
    for selected in combinations:
        current_sum = calculate_vector_sum(coordinates, selected)
        min_sum = min(min_sum, current_sum)

    return min_sum


# Input handling
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    coordinates = [tuple(map(int, input().split())) for _ in range(N)]
    combinations = []
    Combinations(N)

    min_vector_sum = find_min_vector_sum(coordinates)
    print(f'#{t} {min_vector_sum}')
