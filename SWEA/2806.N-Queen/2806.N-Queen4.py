import sys
sys.stdin = open('input.txt')


def n_queen(row=0, cols=None, left_diagonals=None, right_diagonals=None):
    if cols is None:
        cols = set()
    if left_diagonals is None:
        left_diagonals = set()
    if right_diagonals is None:
        right_diagonals = set()

    if row == N:
        return 1

    count = 0
    for col in range(1, N + 1):
        left_diag = row - col
        right_diag = row + col

        if col not in cols and left_diag not in left_diagonals and right_diag not in right_diagonals:
            cols.add(col)
            left_diagonals.add(left_diag)
            right_diagonals.add(right_diag)

            count += n_queen(row + 1, cols, left_diagonals, right_diagonals)

            cols.remove(col)
            left_diagonals.remove(left_diag)
            right_diagonals.remove(right_diag)

    return count


for tc in range(1, int(input()) + 1):
    N = int(input())

    result = n_queen()

    print(f'#{tc} {result}')
