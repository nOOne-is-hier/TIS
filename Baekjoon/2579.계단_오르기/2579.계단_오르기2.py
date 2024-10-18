import sys

sys.stdin = open('input.txt')

def findMaxScore(start=-1,last_step=2, former_state=None, max_score=None):
    if not former_state:
        former_state = [0] * N
    current_state = former_state[:]
    if not max_score:
        max_score = [0]

    # 메모이제이션
    current_key = (start, last_step)
    if current_key in memo:
        if memo[current_key] >= current_state[start]:
            return
    memo[current_key] = current_state[start]

    # base condition
    if start == N - 1:
        max_score[0] = max(max_score[0], current_state[N - 1])
        return

    if last_step == 1 and start != 0:
        if start + 2 < N:
            current_state[start + 2] = current_state[start] + stairs[start + 2]
            findMaxScore(start + 2, 2, current_state, max_score)

    elif last_step == 2 or start == 0:
        if start + 1 < N:
            current_state[start + 1] = current_state[start] + stairs[start + 1]
            findMaxScore(start + 1, 1, current_state, max_score)
        if start + 2 < N:
            current_state[start + 2] = current_state[start] + stairs[start + 2]
            findMaxScore(start + 2, 2, current_state, max_score)

    return max_score[0]

N = int(input())
stairs = [int(input()) for _ in range(N)]
memo = {}
result = findMaxScore()
print(result)
