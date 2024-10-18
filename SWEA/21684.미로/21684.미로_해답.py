import sys
sys.stdin = open('input.txt', 'r')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x):
    global result
    # 종료 조건(기저 조건)
    if y == endy and x == endx:
        result = 1  # correct case
        return

    # 다음 재귀 호출
    for i in range(4):
        newy = y + dy[i]
        newx = x + dx[i]

        # 1번 조건. 범위 밖으로는 못감
        if newy < 0 or newy >= N or newx < 0 or newx >= N:
            continue

        # 2번 조건. 벽이면 못감
        if graph[newy][newx] == 1:
            continue

        # 3번 조건. 방문한 지점은 못감
        if visited[newy][newx]:
            continue

        visited[newy][newx] = 1  # 방문처리
        dfs(newy, newx)  # 다음 좌표로 이동


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, list(input().strip()))) for _ in range(N)]

    starty, startx, endy, endx = 0, 0, 0, 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                starty, startx = i, j

            if graph[i][j] == 3:
                endy, endx = i, j

    visited = [[0] * N for _ in range(N)]
    visited[starty][startx] = 1  # start point
    result = 0
    dfs(starty, startx)
    print(f'#{tc} {result}')






