import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    print(f'#{tc}', end=' ')

    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]
    you_win = False

    for r in range(N):
        for c in range(N):
            if board[r][c] == 'o':

                for dir in range(8):
                    dis = 1

                    while True:
                        nr = r + (dr[dir]*dis)
                        nc = c + (dc[dir]*dis)
                        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
                            dis += 1
                        else:
                            break
                    if dis == 5:
                        you_win = True
                        break

            if you_win:
                break
        if you_win:
            break

    print('YES' if you_win else 'NO')
