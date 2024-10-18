import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))

    pollens = [list(map(int, input().split())) for _ in range(N)]

    # 델타 좌표
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    max_pollen = 0

    # brute force
    for r in range(N):
        for c in range(M):
            current_pollen = pollens[r][c]
            total_pollen = current_pollen
            for dir in range(4):
                for dis in range(1, current_pollen+1):
                    nr = r + (dr[dir]*dis)
                    nc = c + (dc[dir]*dis)
                    if 0 <= nr < N and 0 <= nc < M:
                        total_pollen += pollens[nr][nc]
            if max_pollen < total_pollen:
                max_pollen = total_pollen

    print(f'#{tc} {max_pollen}')