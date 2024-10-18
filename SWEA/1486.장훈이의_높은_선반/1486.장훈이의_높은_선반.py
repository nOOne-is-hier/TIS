import sys

sys.stdin = open('input.txt')


def Powerset(idx=0, current=None, min_tower=None):

    if not current:
        current = []

    if not min_tower:
        min_tower = [10000 * 20]

    if idx == len(S):
        current_sum = sum(current)
        if current_sum == B:
            return 0

        elif B <= current_sum < min_tower[0]:
            min_tower[0] = current_sum

        return min_tower[0]

    result = Powerset(idx + 1, current, min_tower)
    if not result:
        return 0

    current.append(S[idx])
    result = Powerset(idx + 1, current, min_tower)
    current.pop()
    if not result:
        return 0

    return min_tower[0] - B

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    print(f'#{tc} {Powerset()}')