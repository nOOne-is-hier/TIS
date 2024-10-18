import sys

sys.stdin = open('input.txt')

def calculate_vector_sum(coordinates, case, n):
    vector_x, vector_y = 0, 0

    for i in range(n):
        if i in case:
            vector_x += coordinates[i][0]
            vector_y += coordinates[i][1]
        else:
            vector_x -= coordinates[i][0]
            vector_y -= coordinates[i][1]

    return vector_x ** 2 + vector_y ** 2

def Combinations(n, start=0, case=None, is_visited=None, min_sum=float('inf'), coordinates=None):
    if case is None:
        case = []
    if is_visited is None:
        is_visited = [0] * n

    if len(case) == n // 2:
        current_sum = calculate_vector_sum(coordinates, case, n)
        min_sum[0] = min(min_sum[0], current_sum)
        return

    for num in range(start, n):
        if not is_visited[num]:
            is_visited[num] = 1
            case.append(num)
            Combinations(n, num + 1, case, is_visited, min_sum, coordinates)
            case.pop()
            is_visited[num] = 0

# Input handling
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    coordinates = [tuple(map(int, input().split())) for _ in range(N)]
    min_sum = [float('inf')]  # 최소값을 리스트로 감싸서 mutable하게 전달
    Combinations(N, coordinates=coordinates, min_sum=min_sum)

    print(f'#{t} {min_sum[0]}')
