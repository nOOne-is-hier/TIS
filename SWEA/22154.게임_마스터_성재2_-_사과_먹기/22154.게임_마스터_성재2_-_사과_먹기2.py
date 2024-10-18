import sys
sys.stdin = open('input.txt')

# 각 방향을 해싱 (우회전만 가능)
directions = {'up': 0, 'right': 1, 'down': 2, 'left': 3}
reverse_directions = {v: k for k, v in directions.items()}

# 사분면으로 가는 우회전 횟수를 계산하는 딕셔너리
turns_needed = {
        'up':   {1: 1, 2: 2, 3: 3, 4: 3},
        'right': {1: 3, 2: 1, 3: 2, 4: 3},
        'down': {1: 3, 2: 3, 3: 1, 4: 2},
        'left': {1: 2, 2: 3, 3: 3, 4: 1}
    }

# 어느 사분면에 있는지 판단
def which_quadrant(reference_point, next_point):
    cr, cc = map_marker[reference_point]   # 현재 좌표
    nr, nc = map_marker[next_point]        # 다음 좌표

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
    # 상하좌우 같은 축에 있을 경우
    if cr == nr:
        return 'horizontal'
    if cc == nc:
        return 'vertical'


def how_many_rotate(current=0, direction='right', total_count=None):
    if current == goal:
        return
    # 결과를 저장할 변수
    if not total_count:
        total_count = [0]
    # 다음 위치와의 관계
    toward = which_quadrant(current, current + 1)
    # 사분면에 따른 회전 계산
    if type(toward) == int:
        change_direction = turns_needed[direction][toward]
        # 방향 업데이트
        direction = reverse_directions[(directions[direction] + change_direction) % 4]
        total_count[0] += change_direction
        how_many_rotate(current + 1, direction, total_count)
    # 같은 축에 있을 경우
    elif toward == 'horizontal':
        # 오른쪽과 왼쪽 구분
        current_col = map_marker[current][1]
        next_col = map_marker[current + 1][1]
        if (next_col > current_col and direction == 'right') or (next_col < current_col and direction == 'left'):
            # 같은 방향이면 회전 필요 없음
            how_many_rotate(current + 1, direction, total_count)
        else:
            # 반대 방향이면 2번 회전
            direction = reverse_directions[(directions[direction] + 2) % 4]
            total_count[0] += 2
            how_many_rotate(current + 1, direction, total_count)

    elif toward == 'vertical':
        # 위쪽과 아래쪽 구분
        current_row = map_marker[current][0]
        next_row = map_marker[current + 1][0]
        if (next_row > current_row and direction == 'down') or (next_row < current_row and direction == 'up'):
            # 같은 방향이면 회전 필요 없음
            how_many_rotate(current + 1, direction, total_count)
        else:
            # 반대 방향이면 2번 회전
            direction = reverse_directions[(directions[direction] + 2) % 4]
            total_count[0] += 2
            how_many_rotate(current + 1, direction, total_count)

    return total_count[0]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dungeon = [list(map(int, input().split())) for _ in range(N)]

    # 각 좌표를 저장할 list
    map_marker = [(0, 0)] + [0] * 10

    # 좌표 탐색을 리스트 컴프리헨션으로 표현
    list(map(lambda r_c: map_marker.__setitem__(dungeon[r_c[0]][r_c[1]], r_c) if dungeon[r_c[0]][r_c[1]] else None,
             [(r, c) for r in range(N) for c in range(N)]))

    # 최종 목표
    goal = next(10 + cursor + 1 for cursor in range(-1, - 12, -1) if map_marker[cursor])

    # 시뮬레이션
    result = how_many_rotate()

    print(f'#{tc}', result)
