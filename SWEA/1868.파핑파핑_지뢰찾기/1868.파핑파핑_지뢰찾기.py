import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def revealing(r, c, coordinates=[]):
    if any(minesweeper[r][c] == mine_or_flag for mine_or_flag in '*N'):
        return False
    visited_cell[r][c] = 1
    is_uncliked = set()
    for dir in range(8):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N:
            is_uncliked.add(minesweeper[nr][nc])
            if not visited_cell[nr][nc] and is_safe_cell[nr][nc]:
                coordinates.append((nr, nc))
                visited_cell[nr][nc] = 1

    if '*' in is_uncliked:
        minesweeper[r][c] = 'N'
        return False


    minesweeper[r][c] = '0'
    for line in minesweeper:
        print(*line)
    print(click, r, c, coordinates)

    return coordinates


def detecting(r, c):
    if visited_cell[r][c]:
        return False

    for dir in range(8):
        nr = r + dr[dir]
        nc = c + dc[dir]

        if 0 <= nr < N and 0 <= nc < N:
            if minesweeper[nr][nc] == '*':
                is_safe_cell[r][c] = 0
                return False

    if minesweeper[r][c] == 'N':
        for line in minesweeper:
            print(*line)
        print(click, r, c)

    return True


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    minesweeper = [list(input()) for _ in range(N)]
    visited_cell = [[0]*N for _ in range(N)]
    is_safe_cell = [[1]*N for _ in range(N)]

    # 지뢰 방문 처리
    for r in range(N):
        for c in range(N):
            if minesweeper[r][c] == '*':
                visited_cell[r][c] = 1

    # 델타 좌표
    dr = [0, -1, -1, -1, 0, 1, 1, 1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]
    click = 0
    for r in range(N):
        for c in range(N):
            if detecting(r, c):
                click += 1
                array = revealing(r, c)
                while array:
                    y, x = array.pop(0)
                    result = revealing(y, x, array)


    for line in minesweeper:
        print(*line)
    for line in visited_cell:
        print(*line)
    count_dot = 0
    print(click)
    for line in minesweeper:
        count_dot += line.count('.')
    print(f'#{tc} {click+count_dot}')
