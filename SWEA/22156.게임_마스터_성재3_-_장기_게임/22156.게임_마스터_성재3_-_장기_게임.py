import sys
sys.stdin = open('input.txt')

# 델타 배열
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def count_captured_pawns(start, captured_pawns=None, remaining_turns=3, current_captured=None, former_state=None):
    # 결과 변수
    if not captured_pawns:
        captured_pawns = [0]
    # 쫄을 담을 포켓 생성
    if not current_captured:
        current_captured = set()
    # 중복 경로 백트래킹
    if not former_state:
        former_state = {}
    # 이미 같은 상태에서 남은 턴을 탐색한 경우라면 캐싱된 결과를 반환
    key = start, remaining_turns
    # if key in former_state:
    #     return
    # 상태 기록
    former_state[key] = True
    # 탐색 시작
    y, x = start
    for dir in range(4):
        distance = 1
        can_jump = False
        # 경계 설정
        while True:
            # 범위를 벗어나면 탐색 종료
            ny = y + (dr[dir] * distance)
            nx = x + (dc[dir] * distance)
            if not (0 <= ny < N and 0 <= nx < N):
                break
            # 다른 말이 있어야 이동 가능
            if not can_jump:
                if board[ny][nx]:
                    can_jump = True
            # 이동 가능하다면
            else:
                # 쫄을 먹은 경우
                if board[ny][nx] and (ny, nx) not in current_captured:
                    next_pos = (ny, nx)
                    # 해당 쫄을 처음 잡은 경우
                    board[ny][nx] = 1
                    captured_pawns[0] += 1
                    current_captured.add(next_pos)
                    print((ny, nx), remaining_turns)
                    # 기저 조건
                    if remaining_turns > 1:
                        count_captured_pawns(next_pos, captured_pawns, remaining_turns - 1, current_captured, former_state)
                    # 백트래킹
                    board[ny][nx] = 0
                # 이미 먹었거나 빈 칸인 경우
                elif not board[ny][nx] or (ny, nx) not in current_captured:
                    next_pos = (ny, nx)
                    # 기저 조건
                    if remaining_turns > 1:
                        count_captured_pawns(next_pos, captured_pawns, remaining_turns - 1, current_captured, former_state)
            # 거리 증가
            distance += 1
    return captured_pawns[0]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 시작점 탐색
    cannon_pos = next((r, c) for r in range(N) for c in range(N) if board[r][c] == 2)
    # 포의 위치를 0으로 변경
    board[cannon_pos[0]][cannon_pos[1]] = 0

    result = count_captured_pawns(cannon_pos)
    print(result)
    # print(f'#{tc}', len(result))