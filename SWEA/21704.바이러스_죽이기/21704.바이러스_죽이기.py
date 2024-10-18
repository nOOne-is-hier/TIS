import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, P = list(map(int, input().split()))

    # 바이러스 배열
    virus_plate = [list(map(int, input().split())) for _ in range(N)]

    # 델타 좌표
    dx = [[0]*P, [(1+x) for x in range(P)], [0]*P, [(-1-x) for x in range(P)]]
    dy = [[(1+y) for y in range(P)], [0]*P, [(-1-y) for y in range(P)], [0]*P]

    # 최대값을 저장하기 위한 변수
    max_kill = 0

    # 탐색 시작, brute force
    for r in range(N):
        for c in range(N):
            dead_virus = 0

            # 4방위
            for i in range(4):
                for j in range(P):
                    nr = r + dx[i][j]
                    nc = c + dy[i][j]

                    if 0 <= nr < N and 0 <= nc < N:
                        dead_virus += virus_plate[nr][nc]

            dead_virus += virus_plate[r][c]

            if dead_virus > max_kill:
                max_kill = dead_virus

    # 결과 출력
    print(f'#{tc} {max_kill}')
