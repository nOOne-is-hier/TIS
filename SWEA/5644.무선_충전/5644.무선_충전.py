import sys
sys.stdin = open('input.txt')
from collections import defaultdict, deque

# 델타 값
direction = {0: (0, 0), 1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}

# 딕셔너리에 좌표를 key로 power와 tag기록
def mapping_coordinates(column, row, charge_range, power, tag, is_visited=None):
    if not is_visited:
        is_visited = [[0] * 10 for _ in range(10)]
        is_visited[row][column] = 1
    charge_points[(row, column)].append((power, tag))
    order = deque([(row, column, 0)])
    while order:
        r, c, level = order.popleft()
        # 기저 조건
        if level >= charge_range:
            break
        for dir in range(1, 5):
            nr = r + direction[dir][0]
            nc = c + direction[dir][1]
            if 0 <= nr < 10 and 0 <= nc < 10 and not is_visited[nr][nc]:
                is_visited[nr][nc] = 1
                charge_points[(nr, nc)].append((power, tag))
                order.append((nr, nc, level + 1))


def calculate_best_charge(A, B):
    # 둘 다 충전이 불가능 하면 return
    if A not in charge_points and B not in charge_points:
        return 0
    # 둘 중 하나만 가능 하면
    elif A in charge_points and B not in charge_points:
        return sorted(charge_points[A])[-1][0]
    elif B in charge_points and A not in charge_points:
        return sorted(charge_points[B])[-1][0]

    # 해시로 접근
    usable_A = sorted(charge_points[A])
    usable_B = sorted(charge_points[B])
    # 서로 다른 것을 이용할 수 있다면 return
    if usable_A[-1][-1] != usable_B[-1][-1]:
        return usable_A[-1][-2] + usable_B[-1][-2]
    # 서로 같은 것을 이용해야 한다면 대안 탐색
    else:
        # 이용가능한 BC가 한 개 뿐이라면
        if len(usable_A) == len(usable_B) == 1:
            return usable_A[-1][-2]
        # 두 개 이상인 경우가 있다면
        elif len(usable_A) > 1 and len(usable_B) > 1:
            return usable_B[-1][-2] + max(usable_A[-2][-2], usable_B[-2][-2])
        elif len(usable_A) > 1:
            return usable_A[-2][-2] + usable_B[-1][-2]
        elif len(usable_B) > 1:
            return usable_B[-2][-2] + usable_A[-1][-2]

T = int(input())

for tc in range(1, T + 1):
    M, A = map(int, input().split())    # 이동 시간, BC의 수
    A_order = [0] + list(map(int, input().split()))
    B_order = [0] + list(map(int, input().split()))
    # 좌표를 기준으로 BC의 성능과 매핑
    charge_points = defaultdict(list)
    for tag in range(A):
        c, r, C, P = map(int, input().split())  # x, y, 충전 범위, 출력량
        mapping_coordinates(c - 1, r - 1, C, P, tag)
    # 시뮬레이션 시작
    result = 0
    Ar = Ac = 0
    Br = Bc = 9
    for trace in range(M + 1):
        Ar += direction[A_order[trace]][0]
        Ac += direction[A_order[trace]][1]
        Br += direction[B_order[trace]][0]
        Bc += direction[B_order[trace]][1]
        result += calculate_best_charge((Ar, Ac), (Br, Bc))

    print(f'#{tc}', result)