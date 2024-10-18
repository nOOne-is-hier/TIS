import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, M = list(map(int, input().split()))
    heritage_site = [list(map(int, input().split())) for _ in range(N)]
    is_visited = [[0]*M for _ in range(N)]

    # 델타 배열
    dr = [0, 1]
    dc = [1, 0]

    longest_structure = 0
    for r in range(N):
        for c in range(M):
            if heritage_site[r][c] and not is_visited[r][c]:
                is_visited[r][c] = 1
                for dir in range(2):
                    dis = 1
                    while True:
                        nr = r + (dr[dir] * dis)
                        nc = c + (dc[dir] * dis)
                        if nr < N and nc < M:
                            is_visited[nr][nc] = 1
                            if heritage_site[nr][nc]:
                                dis += 1
                            else:
                                break
                        else:
                            break
                    if longest_structure < dis:
                        longest_structure = dis

    if longest_structure == 1:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {longest_structure}')