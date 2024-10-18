# S: 시작 지점, E: 출구, L: 레버, O: 통로, X: 벽
from collections import deque

def solution(maps):
    # 델타 배열
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    height = len(maps)
    width = len(maps[0])
    is_visitedS = [[0] * width for _ in range(height)]
    is_visitedE = [line[:] for line in is_visitedS[:]]

    lever = next((r, c, 0) for r in range(height) for c in range(width) if maps[r][c] == 'L')

    # 레버에서 시작과 도착점의 최단거리를 탐색
    to_start = deque([lever])
    is_visitedS[lever[0]][lever[1]] = 1
    to_end = deque([lever])
    is_visitedE[lever[0]][lever[1]] = 1
    how_far_to_start = how_far_to_end = -1

    # 두 개의 큐를 동시에 순회하지 않고, 순차적으로 수행하여 시간 초과 문제를 방지
    while to_start:
        start_r, start_c, s_distance = to_start.popleft()

        for dir in range(4):
            s_nr = start_r + dr[dir]
            s_nc = start_c + dc[dir]

            if 0 <= s_nr < height and 0 <= s_nc < width and not is_visitedS[s_nr][s_nc] and maps[s_nr][s_nc] != 'X':
                if maps[s_nr][s_nc] == 'S':
                    how_far_to_start = s_distance + 1
                    to_start.clear()
                    break
                else:
                    is_visitedS[s_nr][s_nc] = 1
                    to_start.append((s_nr, s_nc, s_distance + 1))

    while to_end:
        end_r, end_c, e_distance = to_end.popleft()

        for dir in range(4):
            e_nr = end_r + dr[dir]
            e_nc = end_c + dc[dir]

            if 0 <= e_nr < height and 0 <= e_nc < width and not is_visitedE[e_nr][e_nc] and maps[e_nr][e_nc] != 'X':
                if maps[e_nr][e_nc] == 'E':
                    how_far_to_end = e_distance + 1
                    to_end.clear()
                    break
                else:
                    is_visitedE[e_nr][e_nc] = 1
                    to_end.append((e_nr, e_nc, e_distance + 1))

    if how_far_to_start != -1 and how_far_to_end != -1:
        answer = how_far_to_start + how_far_to_end
    else:
        answer = -1

    return answer
