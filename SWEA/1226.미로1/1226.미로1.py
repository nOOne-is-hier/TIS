import sys
sys.stdin = open('input.txt')

for _ in range(10):
    print(f'#{input()}', end=' ')
    maze = [list(map(int, input().strip())) for _ in range(16)]
    '''found = False
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                start = (r, c)
            elif maze[r][c] == 3:
                goal = (r, c)
            if 'start' in locals() and 'goal' in locals():
                found = True
                break
        if found:
            break'''
    start_mirror_set = [[0]*16 for _ in range(16)]
    goal_mirror_set = [[0]*16 for _ in range(16)]
    start = (1, 1); goal = (13, 13)

    start_que = [start]
    goal_que = [goal]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    found = False

    while start_que and goal_que:
        r, c = start_que.pop(0)

        for dir in range(4):
            nr = r + dr[dir]; nc = c + dc[dir]
            if 0 <= nr <= 15 and 0 <= nc <= 15:
                if maze[nr][nc] == 0 and not start_mirror_set[nr][nc]:
                    start_que.append((nr, nc))
                    start_mirror_set[nr][nc] = 1
        if start_mirror_set[nr][nc] == goal_mirror_set[nr][nc] == 1:
            found = True
            print(1); break
        elif maze[nr][nc] == 3:
            found = True
            print(1); break

        r, c = goal_que.pop(0)

        for dir in range(4):
            nr = r + dr[dir]; nc = c + dc[dir]
            if 0 <= nr <= 15 and 0 <= nc <= 15:
                if maze[nr][nc] == 0 and not goal_mirror_set[nr][nc]:
                    goal_que.append((nr, nc))
                    goal_mirror_set[nr][nc] = 1
        if start_mirror_set[nr][nc] == goal_mirror_set[nr][nc] == 1:
            found = True
            print(1); break
        elif maze[nr][nc] == 2:
            found = True
            print(1); break

    if not found:
        print(0)