import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    balloons = list(map(int, input().split()))

    # 메모이제이션 테이블
    former_state = [0] * (1 << N)

    for state in range(1 << N):  # 모든 상태에 대해 순회
        for current in range(N):  # 현재 풍선 위치
            if state & (1 << current):  # 현재 풍선이 이미 터졌다면
                continue  # 건너뛰고, 아직 터지지 않은 풍선을 찾아야 함

            # 현재 풍선이 터지지 않은 상태에서 이곳에서 터뜨리는 작업을 수행
            # 좌우 탐색 및 점수 계산 로직
            left = 1
            right = 1
            is_left = False
            is_right = False

            # 오른쪽 탐색
            r = current + 1
            while r < N:
                if state & (1 << r):  # 이미 터트린 풍선이면 스킵
                    r += 1
                    continue
                else:
                    right = balloons[r]
                    is_right = True
                    break

            # 왼쪽 탐색
            l = current - 1
            while l >= 0:
                if state & (1 << l):  # 이미 터트린 풍선이면 스킵
                    l -= 1
                    continue
                else:
                    left = balloons[l]
                    is_left = True
                    break

            # 점수 계산
            if is_left and is_right:
                current_score = right * left
            elif is_left:
                current_score = left
            elif is_right:
                current_score = right
            else:
                current_score = balloons[current]

            # 상태 메모
            new_state = state | (1 << current)  # 현재 풍선을 터뜨린 상태로 전이
            former_state[new_state] = max(former_state[new_state], former_state[state] + current_score)

    # 최종 결산
    print(f'#{tc} {former_state[(1 << N) - 1]}')
