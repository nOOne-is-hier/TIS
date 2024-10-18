import sys

sys.stdin = open('input.txt')


def DFS(current_position=-1, current_score=0, max_score=None):
    if max_score == None:
        max_score = [-float('INF')]

    # 기저조건
    if current_position >= N:
        max_score[0] = max(current_score, max_score[0])
        return

    # 메모이제이션
    current_state = (current_position, current_score)
    if current_state in former_state:
        return
    former_state.add(current_state)

    second_addend1 = 0
    second_addend2 = 0
    if current_position + 2 < N:
        second_addend1 = game_map[current_position + 2]
    if current_position + 7 < N:
        second_addend2 = game_map[current_position + 7]
    DFS(current_position + 2, current_score + second_addend1, max_score)
    DFS(current_position + 7, current_score + second_addend2, max_score)

    return max_score[0]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    game_map = list(map(int, input().split()))
    former_state = set()
    result = DFS()
    print(f'#{tc}', result)
