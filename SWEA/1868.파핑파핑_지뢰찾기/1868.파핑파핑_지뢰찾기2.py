import sys
sys.stdin = open('input.txt')


def is_safe(r, c):
    """ 현재 좌표 (r, c) 가 지뢰가 없는 안전한 칸인지 확인 """
    if 0 <= r < N and 0 <= c < N and not visited[r][c] and minesweeper[r][c] != '*':
        return True
    return False

def bfs(r, c):
    """ BFS를 사용해 연결된 안전한 구역을 탐색하고, 한 번의 클릭으로 열 수 있는 칸을 모두 엽니다. """
    queue = [(r, c)]
    visited[r][c] = True

    while queue:
        cr, cc = queue.pop(0)

        # 현재 칸이 0이라면 주변 칸들도 열기 위해 큐에 추가
        if minesweeper[cr][cc] == '0':
            for dir in range(8):
                nr, nc = cr + dr[dir], cc + dc[dir]
                if is_safe(nr, nc):
                    visited[nr][nc] = True
                    queue.append((nr, nc))

def count_adjacent_mines(r, c):
    """ 현재 좌표 (r, c) 주변에 지뢰가 몇 개 있는지 계산 """
    count = 0
    for dir in range(8):
        nr, nc = r + dr[dir], c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N and minesweeper[nr][nc] == '*':
            count += 1
    return count

def preprocess_board():
    """ 보드를 미리 처리하여 각 칸이 지뢰인지 아닌지 계산합니다. """
    for r in range(N):
        for c in range(N):
            if minesweeper[r][c] == '.':
                minesweeper[r][c] = str(count_adjacent_mines(r, c))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    minesweeper = [list(input()) for _ in range(N)]

    # 델타 좌표 (상하좌우 대각선)
    dr = [0, -1, -1, -1, 0, 1, 1, 1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    # 보드를 미리 처리하여 각 칸이 지뢰인지 아닌지 계산
    preprocess_board()

    # 방문 여부를 추적하기 위한 배열
    visited = [[False] * N for _ in range(N)]
    click = 0

    # 1. 0인 위치부터 우선적으로 BFS로 탐색하여 한 번의 클릭으로 열 수 있는 구역을 찾는다.
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and minesweeper[r][c] == '0':
                bfs(r, c)
                click += 1

    # 2. 아직 방문하지 않은 안전한 칸이 있으면 개별적으로 클릭한다.
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and minesweeper[r][c] != '*' and minesweeper[r][c] != '0':
                click += 1

    # 모든 칸이 '.'인 경우, 전체 보드가 1 클릭으로 열리게 합니다.
    if click == 0:
        click = 1
    # 결과 출력
    print(f'#{tc} {click}')
