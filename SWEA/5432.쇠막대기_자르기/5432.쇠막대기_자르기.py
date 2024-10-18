import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    brackets = input()

    bars = 0
    pieces = 0

    for idx in range(0, len(brackets)-1):
        if brackets[idx] == chr(40) and brackets[idx+1] == chr(41):
            pieces += bars

        elif brackets[idx] == chr(41) and brackets[idx+1] == chr(40):
            continue

        elif brackets[idx] == chr(40):
            bars += 1
            pieces += 1

        elif brackets[idx] == chr(41):
            bars -= 1

    print(f'#{tc} {pieces}')