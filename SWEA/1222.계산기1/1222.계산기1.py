import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    length = input()
    infix_notation = input()
    postfix_notation = []
    operators = []
    print(f'#{tc}', end=' ')
    for token in infix_notation:
        if token in map(str, list((range(10)))):
            postfix_notation.append(token)

        elif not operators and token == '+':
            operators.append(token)

        elif token == operators[-1]:
            postfix_notation.append(operators.pop())
            operators.append(token)

    for operator in operators[::-1]:
        postfix_notation.append(operator)

    calculate = []
    for token in postfix_notation:
        if token.isdigit():
            calculate.append(int(token))

        elif token == '+':
            last = calculate.pop()
            second_last = calculate.pop()
            calculate.append(last + second_last)

    print(*calculate)