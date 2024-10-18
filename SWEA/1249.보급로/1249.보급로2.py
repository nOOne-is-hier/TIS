import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(row, column, current_cost):

    # 유효하지 않은 좌표 가지치기
    if current_cost >= min_cost:
        return
    # 방문 안 했다면 방문 처리 후 원본 갱신
    if type(is_visited[row][column]) == type(None):
        # 해당 좌표의 파손도는 별도로 보관
        is_visited[row][column] = ardennes[row][column]
        current_cost += ardennes[row][column]
        ardennes[row][column] = current_cost
    # 방문 했다면 내가 들고온 값과 비교
    else:
        current_cost += is_visited[row][column]
        if ardennes[row][column] > current_cost:
            ardennes[row][column] = current_cost
        # 가지치기
        else:
            return

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N:
            orders.append((nr, nc, current_cost))


for tc in range(1, int(input()) + 1):
    N = int(input())
    ardennes = [list(map(int, list(input()))) for _ in range(N)]
    is_visited = [[None] * N for _ in range(N)]
    orders = deque([(0, 0, ardennes[0][0])])
    min_cost = N ** 2 * 9

    # 4방위 이동
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # BFS 시작
    while orders:
        r, c, current_cost = orders.popleft()
        BFS(r, c, current_cost)
    print(f'#{tc} {ardennes[N-1][N-1]}')