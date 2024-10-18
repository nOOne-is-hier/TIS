import sys
sys.stdin = open('input.txt')

# stack을 이용해 풀겠다!
# '#'은 종료조건이다!!
T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    fire_range = int(input())
    plan = [list(map(str, input())) for _ in range(N)]

    # 델타 좌표
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 폭탄 위치 탐색
    bombs = []

    for r in range(N):
        for c in range(M):
            if plan[r][c] == chr(64):
                bombs += [(r, c)]

    # 발파 시작

    while bombs:
        r, c = bombs.pop()
        plan[r][c] = chr(37)
        # 4방위
        for dir in range(4):
            # 벽을 만났는가?
            is_blocked = False
            # 폭발 범위 만큼 탐색
            for plus_power in range(1, fire_range + 1):
                nr = r + (dr[dir]*plus_power)
                nc = c + (dc[dir]*plus_power)

                # 우선 영역 안인가?
                if 0 <= nr < N and 0 <= nc < M:
                    if plan[nr][nc] == chr(35):
                        is_blocked = True
                        break
                    plan[nr][nc] = chr(37)
            # 벽을 만났으면 해당 방위는 건너뛰어라
            else:
                if is_blocked:
                    continue

    print(f'#{tc}')
    for line in plan:
        print(''.join(line))