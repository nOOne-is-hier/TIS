import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    box1, box2, box3 = map(int, input().split())

    subtrahend1 = subtrahend2 = 0
    if box3 <= box2:
        subtrahend1 = (box2 - box3) + 1
        box2 -= subtrahend1
    if box2 <= box1:
        subtrahend2 = (box1 - box2) + 1
        box1 -= subtrahend2

    if box1 < 1 or box2 < 1:
        print(-1)

    else:
        result = subtrahend2 + subtrahend1
        print(result)