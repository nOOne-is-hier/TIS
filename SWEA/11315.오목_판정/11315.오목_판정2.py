import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

# 사용자 정의 예외
class WinException(Exception):
    pass

# 델타 좌표 (8방향: 우, 우하, 하, 좌하, 좌, 좌상, 상, 우상)
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def check_five_in_a_row(r, c, dir, count):
    if count == 5:  # 5개의 돌이 연속해서 존재하면 예외 발생
        raise WinException

    nr = r + dr[dir]
    nc = c + dc[dir]

    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
        check_five_in_a_row(nr, nc, dir, count + 1)

for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    try:
        for r in range(N):
            for c in range(N):
                if board[r][c] == 'o':
                    for dir in range(8):
                        check_five_in_a_row(r, c, dir, 1)
    except WinException:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
