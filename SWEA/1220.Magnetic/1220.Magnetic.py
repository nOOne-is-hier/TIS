import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    magnetic_field = [list(map(int, input().split())) for _ in range(N)]

    count_frustration = 0
    for c in range(N):
        for r in range(N):
            moving_distance = 0
            nr = r + moving_distance
            if magnetic_field[nr][c] == 1:
                while True:
                    nr += 1
                    if nr == N:
                        break
                    if magnetic_field[nr][c] == 1:
                        break
                    elif magnetic_field[nr][c] == 2:
                        count_frustration += 1
                        break

    print(f'#{tc} {count_frustration}')