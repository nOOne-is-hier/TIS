import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')

    prairie = input()

    balls = 0

    for idx in range(len(prairie)):
        if prairie[idx] == chr(40):
            if any(prairie[idx+1] == thing for thing in [chr(41), chr(124)]):
                balls += 1

        elif prairie[idx] == chr(41):
            if prairie[idx-1] == chr(124):
                balls += 1

    print(balls)