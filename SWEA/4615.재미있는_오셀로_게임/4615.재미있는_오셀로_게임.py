import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, M = list(map(int, input().split()))

    # 초기 배치
    board = [[0] * N for _ in range(N)]
    board[N // 2][N // 2] = board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2][N // 2 - 1] = board[N // 2 - 1][N // 2] = 1

    # 델타 좌표
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    # 입력에 따라 게임 진행
    for _ in range(M):
        r, c, stone = list(map(int, input().split()))
        r -= 1;
        c -= 1
        board[r][c] = stone

        for dir in range(8):

            coordinates = []
            dis = 1

            while True:
                nr = r + (dr[dir] * dis)
                nc = c + (dc[dir] * dis)
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] == 0:
                        coordinates = []
                        break

                    elif board[nr][nc] == stone:
                        for y, x in coordinates:
                            board[y][x] = stone
                        break

                    else:
                        coordinates += [[nr, nc]]
                        dis += 1
                else:
                    break

    print(f'#{tc} {sum(line.count(1) for line in board)} {sum(line.count(2) for line in board)}')
