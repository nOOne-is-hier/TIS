import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    game_map = list(map(int, input().split()))
    state_tracker = [-21e9] * N
    print(f'#{tc}', end=' ')

    state_tracker[1] = game_map[1]
    if N > 6:
        state_tracker[6] = game_map[6]
    for idx in range(3, N, 2):
        if idx >= 6:
            break
        state_tracker[idx] = state_tracker[idx - 2] + game_map[idx]

    for idx in range(7, N):
        state_tracker[idx] = max(state_tracker[idx - 2], state_tracker[idx - 7]) + game_map[idx]
    if N <= 6:
        result = max(0, max(state_tracker[-7:]))
    else:
        result = max(state_tracker[-7:])
    print(result)
