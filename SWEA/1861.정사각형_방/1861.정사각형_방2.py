import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    is_visited = [0] * (N ** 2 + 1)

    # 델타 배열
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 인접한 방 체크
    for r in range(N):
        for c in range(N):
            current = rooms[r][c]
            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]
                if 0 <= nr < N and 0 <= nc < N:
                    if rooms[nr][nc] == current + 1:
                        is_visited[current] = 1
                        break

    # 탐색 후 결과 처리
    result = (0, 0)  # (시작 숫자, 최대 길이)
    start = 1

    while start <= N ** 2:
        if is_visited[start]:  # 유망하다면 탐색 시작
            length = 2
            current_start = start
            while start + 1 <= N ** 2 and is_visited[start + 1]:
                start += 1
                length += 1
            result = max(result, (current_start, length), key=lambda x: (x[1], -x[0]))
        start += 1

    print(f'#{tc}', *result)