import sys
sys.stdin = open('input.txt')
from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    # 델타 배열
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 탐색 시작
    result = (0, 0)
    for r in range(N):
        for c in range(N):
            if rooms[r][c] != -1:
                last = rooms[r][c]
                lr, lc = r, c
                orders = deque([(r, c)])
                distance = 1

                while orders:
                    cr, cc = orders.popleft()
                    found_next = False  # 다음으로 이동할 수 있는지 여부
                    is_promising = False  # 유망한 노드인지 여부

                    for dir in range(4):
                        nr = cr + dr[dir]
                        nc = cc + dc[dir]

                        # 범위 내에 있는 경우
                        if 0 <= nr < N and 0 <= nc < N:
                            # 1 큰 값으로만 이동
                            if rooms[nr][nc] == rooms[cr][cc] + 1:
                                orders.append((nr, nc))
                                distance += 1
                                found_next = True
                                break
                            # 1 작은 값이 인접해 있다면 유망한 노드로 판단
                            elif rooms[nr][nc] == rooms[cr][cc] - 1:
                                is_promising = True

                    # 1 작은 값도 없고, 이동할 수 있는 1 큰 값도 없을 때만 -1로 설정
                    if not found_next and not is_promising:
                        rooms[cr][cc] = -1

                # 결과 갱신
                if distance > 1:
                    result = min(result, (last, distance), key=lambda x: (-x[1], x[0]))

    # 탐색 결과 출력
    print(f'#{tc}', *result)
