import sys
sys.stdin = open('input.txt')

from collections import deque

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())

    # grid
    culture_plate = [[[] for _ in range(N)] for _ in range(N)]

    # 상하좌우 이동을 위한 딕셔너리
    directions = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    
    # 반전 처리를 위한 딕셔너리
    opposite_directions = {1: 2, 2: 1, 3: 4, 4: 3}

    # 주시할 좌표들(r, c, direction)
    coordinates = deque()

    # 입력 완료
    for _ in range(K):
        r, c, microorganism, direction = map(int, input().split())
        culture_plate[r][c] += [microorganism]
        coordinates.append((r, c, direction))

    # 시간 M에 도달하면 합계를 출력 후 종료
    now = 0
    while True:
        # 이동 후 후처리를 위한 임시 좌표들
        temp_coordinates = set()
        while coordinates:
            r, c, direction = coordinates.popleft()
            nr = r + directions[direction][0]
            nc = c + directions[direction][1]

            # 경계에 도달했다면 방향을 수정하고, 미생물을 나눠준다
            if nr in {0, N-1} or nc in {0, N-1}:
                direction = opposite_directions[direction]
                culture_plate[r][c][0] //= 2
            # 미생물을 이동 후 임시로 방향과 함께 저장
            culture_plate[nr][nc].append((culture_plate[r][c].pop(0), direction))
            # 후처리를 위한 좌표 저장
            temp_coordinates.add((nr, nc))

        for r, c in temp_coordinates:
            # 충돌이 없으면 그대로 진행
            if len(culture_plate[r][c]) == 1:
                coordinates.append((r, c, culture_plate[r][c][0][1]))
                culture_plate[r][c][0] = culture_plate[r][c][0][0]
            # 충돌이 있으면 방향 변경, 미생물 병합
            else:
                direction = max(culture_plate[r][c])[1]
                microorganism = sum(map(lambda amount: amount[0], culture_plate[r][c]))
                coordinates.append((r, c, direction))
                culture_plate[r][c] = [microorganism]
        # 한 시간 경과
        now += 1
        # M시간 경과 시 종료
        if now == M:
            total_sum = sum(cell for row in culture_plate for column in row for cell in column)
            print(f'#{tc} {total_sum}')
            break