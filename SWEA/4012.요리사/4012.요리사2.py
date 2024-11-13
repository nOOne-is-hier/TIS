import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    synergies = [list(map(int, input().split())) for _ in range(N)]

    # 결과 초기화
    min_result = float('inf')
    half_size = N // 2

    # 반쪽만 탐색
    for mask in range(1 << N):
        if bin(mask).count('1') != half_size:
            continue

        team_a = [i for i in range(N) if mask & (1 << i)]
        team_b = [i for i in range(N) if not (mask & (1 << i))]

        # 각 팀의 시너지 합 계산
        synergy_a = sum(synergies[i][j] for i in team_a for j in team_a)
        synergy_b = sum(synergies[i][j] for i in team_b for j in team_b)

        # 시너지 차이의 절댓값이 최소인 경우 갱신
        diff = abs(synergy_a - synergy_b)
        min_result = min(min_result, diff)

        # 조기 종료 조건
        if min_result == 0:
            break

    print(f'#{tc}', min_result)
