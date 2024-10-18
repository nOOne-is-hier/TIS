import sys

sys.stdin = open('input.txt')

T = int(input())

def coordinates_in_set(a, b, c, d):
    coordinates = set()
    dx = -1
    for row in range(c-a+1):
        dy = -1
        dx += 1
        for column in range(d-b+1):
            dy += 1
            coordinates.add((a+dx, b+dy))

    return coordinates

for tc in range(1, T + 1):
    N = int(input())
    red_set = set()
    blue_set = set()
    for square in range(N):
        sx, sy, ex, ey, color = list(map(int, input().split()))
        if color == 1:
            red_set.update(coordinates_in_set(sx, sy, ex, ey))

        elif color == 2:
            blue_set.update(coordinates_in_set(sx, sy, ex, ey))

    purple_set = red_set.intersection(blue_set)

    print(f'#{tc}', len(purple_set))
