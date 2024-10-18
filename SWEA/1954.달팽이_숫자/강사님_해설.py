import sys
sys.stdin = open('input.txt', 'r')

# 델타 배열
# 우, 하, 좌, 상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 방문 체크: 숫자가 들어있는 곳은 다시 못가도록
    snails = [[0] * N for _ in range(N)]

    # 시작점(좌표, 바라보고 있는 방향), 반복 조건(1~N*N)
    # 0,0 좌표 / dir: 시작 방향(우측 = 0)
    y, x, dir = 0, 0, 0
    for i in range(1, N*N + 1):
        snails[y][x] = i
        # 다음 좌표 체크용
        new_y = y + dy[dir]
        new_x = x + dx[dir]

        # 범위를 넘어가거나, 이미 방문한 곳이라면
        # 방향을 변환
        if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N or snails[new_y][new_x]:
            # 0 1 2 3 을 반복하도록 4로 나누어 준다.
            dir = (dir + 1) % 4

        y = y + dy[dir]
        x = x + dx[dir]

    print(f'#{tc}')
    for i in range(N):
        print(*snails[i])

