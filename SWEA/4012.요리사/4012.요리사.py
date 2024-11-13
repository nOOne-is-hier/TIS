import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    synergies = [list(map(int, input().split())) for _ in range(N)]
    cases = tuple(combinations(range(N), N // 2))

    length = len(cases)
    f = 0
    e = -1
    min_result = float('inf')
    while f < length // 2:
        F = cases[f]; E = cases[e]
        A = sum(synergies[a][b] for a in F for b in F)
        B = sum(synergies[a][b] for a in E for b in E)
        tmp_diff = abs(A - B)
        min_result = min(min_result, tmp_diff)
        f += 1; e -= 1

    print(f'#{tc}', min_result)
