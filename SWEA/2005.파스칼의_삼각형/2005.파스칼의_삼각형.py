import sys
sys.stdin = open('input.txt')

T = int(input())
def pascal_triangle(height, row, former_line=None):
    if row == 1:
        line = [1]
        print(*line)
        if row == height:
            return
        row += 1
        pascal_triangle(height, row)
    else:
        if row == 2:
            line = [0] * row
            line[0] = line[-1] = 1
            print(*line)
            if row == height:
                return
            row += 1
            former_line = line
            pascal_triangle(height, row, former_line)
        elif row > 2:
            line = [0] * row
            line[0] = line[-1] = 1
            for idx in range(1, row-1):
                line[idx] = former_line[idx-1] + former_line[idx]
            print(*line)
            if row == height:
                return
            row += 1
            former_line = line
            pascal_triangle(height, row, former_line)
    return



for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    pascal_triangle(N, 1)