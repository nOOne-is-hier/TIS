import sys
sys.stdin = open('input.txt')

T = int(input())

def turn_right(matrix):
    mirror_grid = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            mirror_grid[c][r] = str(matrix[r][c])

    for r in range(N):
        mirror_grid[r] = mirror_grid[r][::-1]

    return mirror_grid


for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    rotated_90 = turn_right(grid)
    rotated_180 = turn_right(rotated_90)
    rotated_270 = turn_right(rotated_180)

    print(f'#{tc}')
    for row in range(N):
        print(f"{''.join(rotated_90[row])} {''.join(rotated_180[row])} {''.join(rotated_270[row])}")