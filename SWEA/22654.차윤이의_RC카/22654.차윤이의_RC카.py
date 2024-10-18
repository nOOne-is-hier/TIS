import sys

# 입력 파일 사용 설정
sys.stdin = open('input.txt')

# 델타 탐색 (북, 동, 남, 서 순서)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def simulation(commands, direction=0):
    y, x = start

    for command in commands:
        if command == 'R':
            direction = (direction + 1) % 4
        elif command == 'L':
            direction = (direction + 3) % 4  # 음수 방지
        elif command == 'A':
            ny = y + dr[direction]
            nx = x + dc[direction]

            # 유효한 좌표인지 확인하고 이동
            if 0 <= ny < N and 0 <= nx < N and field[ny][nx] != 'T':
                y, x = ny, nx

    # 목적지 도착 여부 반환
    return (y, x) == end


# 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')

    # 필드 크기와 데이터 입력
    N = int(input())
    field = [input() for _ in range(N)]

    # 시작점과 도착점 탐색
    start = end = None
    for r in range(N):
        for c in range(N):
            if field[r][c] == 'X':
                start = (r, c)
            elif field[r][c] == 'Y':
                end = (r, c)
            # 시작점과 도착점 모두 찾으면 탐색 종료
            if start and end:
                break

    # 명령어 입력 후 시뮬레이션 실행
    Q = int(input())
    for _ in range(Q):
        _, commands = input().split()
        # 결과 출력 (True는 1, False는 0으로 출력)
        print(int(simulation(commands)), end=' ')

    # 테스트 케이스마다 줄바꿈
    print()
