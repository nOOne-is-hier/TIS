import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    # 델타 배열
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # is_visited 배열 초기화: 각 방 번호에 대해 1이 큰 인접한 값이 있는지 기록
    is_visited = [0] * (N ** 2 + 1)

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

    # 후처리: 연속된 유망한 방의 최대 길이와 시작값 계산
    cnt = max_cnt = start = 0

    for i in range(1, N ** 2 + 1):  # 1부터 N^2까지 반복
        if is_visited[i]:
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                start = i - cnt
            cnt = 0

    # 마지막 구간 처리 (마지막 유망 구간이 끝났을 때 갱신되지 않았을 경우 처리)
    if cnt > max_cnt:
        max_cnt = cnt
        start = N * N + 1 - cnt

    # 결과 출력
    print(f'#{tc}', start, max_cnt + 1)
