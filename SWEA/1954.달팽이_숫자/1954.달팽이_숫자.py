import sys

sys.stdin = open('input.txt')

T = int(input())

# 기본 입력 및 빈 그리드 생성
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(range(1, N**2+1))
    grid = [[0]*N for _ in range(N)]

    # 인덱스 증감을 나타낸 행과 열의 델타 리스트 생성_세로열
    mC = []
    start_point = 1
    elem = 0
    for num in range(2*N, 0, -1):
        if start_point % 4 == 1:
            elem = 1
        elif start_point % 2 == 0:
            elem = 0
        if start_point % 4 == 3:
            elem = -1
        start_point += 1
        mC += [elem] * int(num/2)
        mC[0] = 0

    # 인덱스 증감을 나타낸 행과 열의 델타 리스트 생성_가로행
    mR = []
    start_point = 1
    elem = 0
    for num in range(2*N, 0, -1):
        if start_point % 2 == 1:
            elem = 0
        elif start_point % 4 == 2:
            elem = 1
        elif start_point % 4 == 0:
            elem = -1
        start_point += 1
        mR += [elem] * int(num/2)

    # 최종 델타 좌표계 완성
    coordinates = list(zip(mR, mC))

    numbers_idx = 0
    start_r = 0
    start_c = 0
    for x, y in coordinates:
        start_r += x
        start_c += y
        grid[start_r][start_c] = numbers[numbers_idx]
        numbers_idx += 1

    print(f'#{tc}')
    for row in grid:
        print(*row)