import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    side, length = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(side)]
    cell = 0

    # 행에 대해 글자가 들어갈 공간을 탐색
    for row in grid:
        length_of_1 = 1
        for c in range(1, side):
            if row[c-1] == row[c] == 1:
                length_of_1 += 1
                if c == side - 1:
                    if length_of_1 == length:
                        cell += 1
                    length_of_1 = 1
                elif row[c] != row[c+1]:
                    if length_of_1 == length:
                        cell += 1
                    length_of_1 = 1
    # 열에 대해 글자가 들어갈 공간을 탐색
    for c in range(side):
        length_of_1 = 1
        for r in range(1, side):
            if grid[r-1][c] == grid[r][c] == 1:
                length_of_1 += 1
                if r == side - 1:
                    if length_of_1 == length:
                        cell += 1
                    length_of_1 = 1
                elif grid[r][c] != grid[r+1][c]:
                    if length_of_1 == length:
                        cell += 1
                    length_of_1 = 1

    print(f'#{tc}', cell)