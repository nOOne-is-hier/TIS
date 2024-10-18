import sys

sys.stdin = open('input.txt')

# 델타 배열
dr = [-1, -1, -1]
dc = [-1, 0, 1]

T = int(input())

for tc in range(1, T + 1):
    height, width = map(int, input().split())
    the_way_home = [list(map(int, input().split())) for _ in range(height)]
    for col in range(1, width):
        the_way_home[0][col] = 0

    for row in range(1, height):
        for col in range(width):
            if the_way_home[row][col]:  # 벽이 아닐 것
                formal_value = the_way_home[row][col]
                for dir in range(3):
                    nr = row + dr[dir]
                    nc = col + dc[dir]
                    if 0 <= nr < height and 0 <= nc < width:
                        if the_way_home[nr][nc]:    # 벽이 아니어야 함
                            if the_way_home[row][col] == formal_value:  # 갱신이 안 됨
                                the_way_home[row][col] += the_way_home[nr][nc]
                            else:   # 갱신 되었다면 최대값 비교
                                the_way_home[row][col] = max(the_way_home[row][col], formal_value + the_way_home[nr][nc])
                # 갱신이 되지 않았다면 유효하지 않은 경로(벽으로 취급)
                if the_way_home[row][col] == formal_value:
                    the_way_home[row][col] = 0
    result = max(the_way_home[height - 1])
    print(f'#{tc}', result)
