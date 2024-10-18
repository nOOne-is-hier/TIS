import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    # 지도 생성
    N = int(input())
    town_map = [input().split() for _ in range(N)]

    # 중계기 위치 탐색
    found = False

    for r in range(N):
        for c in range(N):
            if town_map[r][c] == '2':
                reapter_r = r
                reapter_c = c
                found = True
                break
        else:
            if found:
                break

    # 최소 반지름 탐색
    min_radius = 0

    for r in range(N):
        for c in range(N):
            if town_map[r][c] == '1':
                if r == reapter_r:
                    radius = abs(reapter_c-c)
                elif c == reapter_c:
                    radius = abs(reapter_r-r)
                else:
                    before_round = str(((reapter_r - r)**2 + (reapter_c - c)**2)**0.5).split('.')

                    if before_round[1] != '0':
                        radius = int(before_round[0]) + 1

                    else:
                        radius = int(before_round[0])

                if min_radius < radius:
                    min_radius = radius

    print(f'#{tc} {min_radius}')