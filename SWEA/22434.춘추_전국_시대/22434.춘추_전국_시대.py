import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    populations = list(map(int, input().split()))
    parents = [idx for idx in range(N)]
    T = int(input())
    for _ in range(T):
        state, nation1, nation2 = input().split()
        nation1 = ord(nation1) - 65
        nation2 = ord(nation2) - 65
        if state[0] == 'a':
            representative = max(parents[nation1], parents[nation2])
            will_change = min(parents[nation1], parents[nation2])
            population = populations[nation1] + populations[nation2]
            populations[representative] = population
            for idx in range(N):
                if parents[idx] == will_change:
                    parents[idx] = representative
                    populations[idx] = population
        else:
            if populations[nation1] == populations[nation2]:
                alliance1 = parents[nation1]
                alliance2 = parents[nation2]
                for idx in range(N):
                    if parents[idx] == alliance1 or parents[idx] == alliance2:
                        populations[idx] = 0
            else:
                lose_country = parents[min((populations[nation1], nation1), (populations[nation2], nation2))[1]]
                for idx in range(N):
                    if parents[idx] == lose_country:
                        populations[idx] = 0
    result = sum(1 for population in populations if population)
    print(f'#{tc}', result)
