import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    notation = input().split()
    operands = []

    for token in notation:

        if token.isdigit():
            operands.append(int(token))

        elif token == chr(43) and len(operands) >= 2:
            last = operands.pop()
            second_last = operands.pop()
            operands.append(second_last + last)

        elif token == chr(45) and len(operands) >= 2:
            last = operands.pop()
            second_last = operands.pop()
            operands.append(second_last - last)

        elif token == chr(42) and len(operands) >= 2:
            last = operands.pop()
            second_last = operands.pop()
            operands.append(second_last * last)

        elif token == chr(47) and len(operands) >= 2:
            last = operands.pop()
            second_last = operands.pop()
            operands.append(second_last // last)

        elif token == chr(46) and len(operands) >= 1:
            print(f'#{tc} {operands.pop()}')

        else:
            print(f'#{tc} error')
            break