import sys
sys.stdin = open('input.txt')


def dfs(r, c, start, is_visited=None, dir=0, right=0, below=0):

    # 방문처리
    if not is_visited:
        is_visited = set()

    is_visited.add(dessert_cafes[r][c])

    # 탐색 시작
    dis = 0
    # 우하로 움직일 때
    if dir == 0:
        while True:
            dis += 1
            nr = r + (dr[dir] * dis)
            nc = c + (dc[dir] * dis)
            if 0 <= nr < N and 0 <= nc < N and dessert_cafes[nr][nc] not in is_visited:
                is_visited.add(dessert_cafes[nr][nc])
                # 방향 전환
                dfs(nr, nc, start, is_visited.copy(), 1, dis)
            else:
                break
    # 좌하로 움질일 때
    if dir == 1:
        while True:
            dis += 1
            nr = r + (dr[dir] * dis)
            nc = c + (dc[dir] * dis)
            if 0 <= nr < N and 0 <= nc < N and dessert_cafes[nr][nc] not in is_visited:
                is_visited.add(dessert_cafes[nr][nc])
                # 방향 전환
                dfs(nr, nc, start, is_visited.copy(), 2, right, dis)
            else:
                break
    # 좌상으로 움직일 때
    if dir == 2:
        while dis != right:
            dis += 1
            nr = r + (dr[dir] * dis)
            nc = c + (dc[dir] * dis)
            if 0 <= nr < N and 0 <= nc < N and dessert_cafes[nr][nc] not in is_visited:
                is_visited.add(dessert_cafes[nr][nc])
            else:
                break
            # 방향 전환
            dfs(nr, nc, start, is_visited.copy(), 3, right, below)
    # 우상으로 움직일 때
    if dir == 3:
        while dis != below:
            dis += 1
            nr = r + (dr[dir] * dis)
            nc = c + (dc[dir] * dis)
            if (nr, nc) == start:
                result.append(len(is_visited))
                break
            elif 0 <= nr < N and 0 <= nc < N and dessert_cafes[nr][nc] not in is_visited:
                is_visited.add(dessert_cafes[nr][nc])
            else:
                break


for tc in range(1, int(input()) + 1):
    N = int(input())
    # 상권 지도
    dessert_cafes = [list(map(int, input().split())) for _ in range(N)]

    # 한 방향 탐색
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]

    # 출발지점
    starts = [(r, c) for r in range(N - 2) for c in range(1, N - 1)]
    result = [-1]

    while starts:
        r, c = starts.pop()
        dfs(r, c, (r, c))
    print(f'#{tc} {max(result)}')