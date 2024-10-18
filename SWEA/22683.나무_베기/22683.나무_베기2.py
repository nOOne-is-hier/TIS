import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')

# 델타 배열 (상, 우, 하, 좌 이동을 위한 방향)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    field = [list(input().strip()) for _ in range(N)]

    # 시작점과 목표 위치 찾기
    start = goal = None
    for r in range(N):
        for c in range(N):
            if field[r][c] == 'X':
                start = (r, c)
            elif field[r][c] == 'Y':
                goal = (r, c)
            if start and goal:
                break
        if start and goal:
            break

    # 다익스트라 탐색을 위한 우선순위 큐
    # (조작 횟수, row, column, 방향, 나무 제거 횟수)
    pq = [(0, start[0], start[1], 0, 0)]
    min_controls = [[[[float('inf')] * 4 for _ in range(K + 1)] for _ in range(N)] for _ in range(N)]
    min_controls[start[0]][start[1]][0][0] = 0

    min_control = float('inf')

    while pq:
        controls, r, c, direction, trees_cut = heappop(pq)

        # 종료 조건: 목표 지점 도착
        if (r, c) == goal:
            min_control = min(min_control, controls)
            continue

        # 네 방향 탐색
        for dir in range(4):
            nr, nc = r + dr[dir], c + dc[dir]
            control_count_next = controls
            trees_cut_next = trees_cut

            # 전진 가능한 경우
            if 0 <= nr < N and 0 <= nc < N:
                # 나무 제거 여부 확인 및 조작 횟수 업데이트
                if field[nr][nc] == 'T':
                    if trees_cut < K:
                        trees_cut_next += 1
                    else:
                        continue

                if dir == direction:
                    control_count_next += 1
                elif abs(dir - direction) == 2:
                    control_count_next += 3
                else:
                    control_count_next += 2

                # 방문 조건 갱신 및 우선순위 큐에 추가
                if control_count_next < min_controls[nr][nc][trees_cut_next][dir]:
                    min_controls[nr][nc][trees_cut_next][dir] = control_count_next
                    heappush(pq, (control_count_next, nr, nc, dir, trees_cut_next))

    # 결과 출력
    if min_control == float('inf'):
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {min_control}')