import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    game_map = list(map(int, input().split()))
    state_tracker = [-21e9] * N
    print(f'#{tc}', end=' ')

    if N == 1:
        print(0)
    if N >= 2:
        state_tracker[1] = game_map[1]
        if N < 4:
            print(max(0, state_tracker[1]))
    if N >= 4:
        state_tracker[3] = state_tracker[1] + game_map[3]
        if N < 6:
            print(max(0, max(state_tracker)))
    if N >= 6:
        state_tracker[5] = state_tracker[3] + game_map[5]
        if N < 7:
            print(max(0, max(state_tracker)))
    if N >= 7:
        state_tracker[6] = game_map[6]
        if N < 8:
            print(max(state_tracker))
    if N >= 8:
        for idx in range(7, N):
            state_tracker[idx] = max(state_tracker[idx - 2], state_tracker[idx - 7]) + game_map[idx]
        result = max(state_tracker[-7:])
        print(result)
