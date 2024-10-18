import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    words_grid = [list(input()) for _ in range(5)]
    empty_grid = [[0]*15 for _ in range(5)]

    # 두 격자 병합
    for r in range(5):
        for c in range(len(words_grid[r])):
            empty_grid[r][c] = words_grid[r][c]

    filled_grid = empty_grid
    result = []

    for c in range(15):
        for r in range(5):
            result += [filled_grid[r][c]]

    removed_result = [char for char in result if char != 0]
    print(f"#{tc} {''.join(removed_result)}")