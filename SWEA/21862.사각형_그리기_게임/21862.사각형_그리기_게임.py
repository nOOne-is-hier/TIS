import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    squares = {}

    for r in range(N):
        for c in range(N):
            for y in range(r, N):
                for x in range(c, N):
                    if board[r][c] == board[y][x]:
                        square = (y+1-r) * (x+1-c)
                        squares.setdefault(square, 0)
                        squares[square] += 1
    if squares:
        print(squares[max(squares.keys())])
    else:
        print(0)