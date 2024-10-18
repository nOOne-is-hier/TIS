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
    how_far_to_start = False
    to_end = deque([lever])
    is_visitedE[lever[0]][lever[1]] = 1
    how_far_to_end = False

    while to_start or to_end:
        if (not to_start and not how_far_to_start) or (not to_end and not how_far_to_end):
            break

        if to_start:
            start_r, start_c, s_distance = to_start.popleft()

            for dir in range(4):
                s_nr = start_r + dr[dir]
                s_nc = start_c + dc[dir]

                if 0 <= s_nr < height and 0 <= s_nc < width and not is_visitedS[s_nr][s_nc] and maps[s_nr][s_nc] != 'X':
                    if maps[s_nr][s_nc] == 'S':
                        how_far_to_start = s_distance + 1
                        to_start = False
                    else:
                        is_visitedS[s_nr][s_nc] = 1
                        to_start.append((s_nr, s_nc, s_distance + 1))
        if to_end:
            end_r, end_c, e_distance = to_end.popleft()

            for dir in range(4):
                e_nr = end_r + dr[dir]
                e_nc = end_c + dc[dir]

                if 0 <= e_nr < height and 0 <= e_nc < width and not is_visitedE[e_nr][e_nc] and maps[e_nr][e_nc] != 'X':
                    if maps[e_nr][e_nc] == 'E':
                        how_far_to_end = e_distance + 1
                        to_end = False
                    else:
                        is_visitedE[e_nr][e_nc] = 1
                        to_end.append((e_nr, e_nc, e_distance + 1))

    if how_far_to_start and how_far_to_end:
        answer = how_far_to_start + how_far_to_end

    else:
        answer = -1

    return answer
