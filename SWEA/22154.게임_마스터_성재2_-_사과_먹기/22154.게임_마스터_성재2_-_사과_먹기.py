import sys
sys.stdin = open('input.txt')

# 각 방향을 해싱
directions = {'up': 0, 'left': 1, 'down': 2, 'right': 3}
reverse_directions = {v: k for k, v in directions.items()}


def which_quadrant(reference_point):
    cr, cc = map_marker[reference_point]
    nr, nc = map_marker[reference_point + 1]

    # 1사분면
    if cr > nr and cc < nc:
        return 1
    # 2사분면
    if cr < nr and cc < nc:
        return 2
    # 3사분면
    if cr < nr and cc > nc:
        return 3
    # 4사분면
    if cr > nr and cc > nc:
        return 4
    # 상
    if cc == nc and cr < nr:
        return 'up'
    # 하
    if cc == nc and cr > nr:
        return 'down'
    # 좌
    if cr == nr and cc > nc:
        return 'left'
    # 우
    if cr == nr and cc < nc:
        return 'right'


def how_many_rotate(current=0, direction='right', total_count=None):
    if current == goal:
        return
    # 결과를 저장할 변수
    if not total_count:
        total_count = [0]
    # 다음 위치와의 관계
    toward = which_quadrant(current)
    # 사분면을 반환
    if type(toward) == int:
        change_direction = (directions[direction] + toward) % 4
        if not change_direction:
            change_direction = 4
            # 방향 업데이트
            direction = reverse_directions[(4 - (directions[direction] - change_direction)) % 4]
            total_count[0] += change_direction
            how_many_rotate(current + 1, direction, total_count)
        else:
            # 방향 업데이트
            direction = reverse_directions[(4 - (directions[direction] - change_direction)) % 4]
            total_count[0] += change_direction
            how_many_rotate(current + 1, direction, total_count)
    # 같은 축에 존재
    if type(toward) == str:
        change_direction = (4 - abs(directions[direction] - toward)) % 4
        total_count[0] += change_direction
        how_many_rotate(current + 1, toward, total_count)

    return total_count[0]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dungeon = [list(map(int, input().split())) for _ in range(N)]

    # 각 좌표를 저장할 list
    map_marker = [(0, 0)] + [0] * N

    # 좌표 탐색을 리스트 컴프리헨션으로 표현
    list(map(lambda r_c: map_marker.__setitem__(dungeon[r_c[0]][r_c[1]], r_c) if dungeon[r_c[0]][r_c[1]] else None,
             [(r, c) for r in range(N) for c in range(N)]))

    # 최종 목표
    goal = next(N + cursor + 1 for cursor in range(-1, -N - 1, -1) if map_marker[cursor])

    # 시뮬레이션
    # result = 0
    # for num in range(1, goal):
    #     count how_many_rotate(num, 'right')
    result = how_many_rotate()

    print(result)