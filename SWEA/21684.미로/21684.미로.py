import sys
sys.stdin = open('input.txt')


# 미로를 탐색하는 재귀 함수
def escape_maze(r, c, crossroads=[]):
    maze[r][c] = 1
    # 갈림길 여부 판단, 나아갈 방향 선택
    direction = -1
    iscrossroads = 0

    for idx in range(4):
        nr, nc = r + dr[idx], c + dc[idx]
        if 0 <= nr < N and 0 <= nc < N:

            if maze[nr][nc] == 3:
                return True
            elif maze[nr][nc] == 0:
                iscrossroads += 1
                direction = idx
    # 갈림길 표시
    if iscrossroads >= 2:
        crossroads.append((r, c))

    # 갈 곳이 더 이상 없고 갈림길도 남아있지 않다면 실패
    if iscrossroads == 0 and not crossroads:
        return False

    # 갈 곳이 더 이상 없지만 돌아갈 갈림길이 있다
    if iscrossroads == 0 and crossroads:
        nr, nc = crossroads.pop()
        return escape_maze(nr, nc, crossroads)

    # 실패도 도착도 하지 않았다면 다음칸으로 이동
    if direction != -1:
        return escape_maze(r + dr[direction], c + dc[direction], crossroads)

    return False

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 델타 좌표
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 시작·도착 좌표 탐색
    start_r = start_c = -1

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start_r = r
                start_c = c
                break
        if start_r != -1:
            break
    print(f'#{tc} {int(escape_maze(start_r, start_c))}')