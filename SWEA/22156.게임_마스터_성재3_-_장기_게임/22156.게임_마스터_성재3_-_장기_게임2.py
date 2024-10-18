import sys
sys.stdin = open('input.txt')

# 델타 배열 (우, 하, 좌, 상)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def count_captured_pawns(start, remaining_turns=3, current_captured=None):
    # 현재 먹은 쫄을 기록하는 세트 (중복 방지)
    if current_captured is None:
        current_captured = set()

    # 탐색을 위한 변수
    y, x = start

    # 4방향 탐색 (우, 하, 좌, 상)
    for dir in range(4):
        distance = 1
        can_jump = False  # 말을 뛰어넘기 전까지는 이동 불가
        # 같은 방향으로 계속 탐색 (범위를 벗어나기 전까지)
        while True:
            ny = y + (dr[dir] * distance)
            nx = x + (dc[dir] * distance)

            # 경계를 벗어나면 중단
            if not (0 <= ny < N and 0 <= nx < N):
                break

            # 말을 하나 넘지 않은 경우
            if not can_jump:
                # 말을 만나면 뛰어넘을 준비
                if board[ny][nx] == 1:  # 말이 있으면 뛰어넘을 준비
                    can_jump = True
            else:
                # 쫄을 먹을 수 있는 경우
                if board[ny][nx]:
                    # 쫄을 먹음
                    current_captured.add((ny, nx))  # 중복 방지로 방문 처리
                    # 남은 이동 횟수가 있으면 다른 방향으로 계속 탐색
                    if remaining_turns > 1:
                        # 쫄을 먹었을 때 해당 위치를 0으로 만들고 복원함
                        board[ny][nx] = 0
                        count_captured_pawns((ny, nx), remaining_turns - 1, current_captured)
                        board[ny][nx] = 1
                    break  # 쫄을 잡은 뒤에는 그 방향으로 더 이상 탐색하지 않음

                # 빈 칸인 경우 계속 탐색 가능
                elif not board[ny][nx]:
                    if remaining_turns > 1:
                        count_captured_pawns((ny, nx), remaining_turns - 1, current_captured)
                # 다른 말을 만나면 더 이상 이동 불가

            # 다음 칸으로 이동
            distance += 1

    return len(current_captured)


T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):
    N = int(input())  # N x N 크기의 장기판
    board = [list(map(int, input().split())) for _ in range(N)]  # 장기판 입력

    # 시작점 탐색 (포의 위치)
    cannon_pos = next((r, c) for r in range(N) for c in range(N) if board[r][c] == 2)

    # 포의 위치를 0으로 변경 (탐색에서 포는 더 이상 사용하지 않음)
    board[cannon_pos[0]][cannon_pos[1]] = 0

    # 결과 계산
    result = count_captured_pawns(cannon_pos)

    # 출력
    print(f'#{tc} {result}')
