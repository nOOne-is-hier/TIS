import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, M = list(map(int, input().split()))

    flies = [list(map(int, input().split())) for _ in range(N)]

    dr1 = [0, 1, 0, -1]
    dc1 = [1, 0, -1, 0]

    dr2 = [-1, 1, 1, -1]
    dc2 = [1, 1, -1, -1]

    max_kill = 0
    # 행열을 순회하며 탐색 시작
    for r in range(N):
        for c in range(N):
            kill = flies[r][c]
            for dis in range(1, M):
                for dir in range(4):
                    nr = r + (dr1[dir]*dis)
                    nc = c + (dc1[dir]*dis)

                    if 0 <= nr < N and 0 <= nc < N:
                        kill += flies[nr][nc]

            if max_kill < kill:
                max_kill = kill

            # X 분사에 대해서도 조사
            kill = flies[r][c]
            for dis in range(1, M):
                for dir in range(4):
                    nr = r + (dr2[dir]*dis)
                    nc = c + (dc2[dir]*dis)

                    if 0 <= nr < N and 0 <= nc < N:
                        kill += flies[nr][nc]

            if max_kill < kill:
                max_kill = kill

    print(f'#{tc} {max_kill}')