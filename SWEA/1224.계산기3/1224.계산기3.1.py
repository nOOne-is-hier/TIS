def infix_to_postfix(infix_notation):
    operators = []
    postfix_notation = ''
    value = {'+': 1, '*': 2, '(': 0}

    for token in infix_notation:
        if token.isdigit():
            postfix_notation += token

        elif token == '(':
            operators.append(token)

        elif token == ')':
            while operators and operators[-1] != '(':
                postfix_notation += operators.pop()
            operators.pop()  # Remove '(' from stack

        else:  # token is an operator
            while operators and value[token] <= value[operators[-1]]:
                postfix_notation += operators.pop()
            operators.append(token)

    while operators:
        postfix_notation += operators.pop()

    return postfix_notation


def evaluate_postfix(postfix_notation):
    operands = []

    for token in postfix_notation:
        if token.isdigit():
            operands.append(int(token))
        else:
            b = operands.pop()
            a = operands.pop()
            if token == '*':
                operands.append(a * b)
            elif token == '+':
                operands.append(a + b)

    return operands[0]


# Example usage
if __name__ == "__main__":
    import sys
    sys.stdin = open('input.txt')

    for tc in range(1, 11):
        length = input().strip()
        infix_notation = input().strip()
        postfix_notation = infix_to_postfix(infix_notation)
        result = evaluate_postfix(postfix_notation)

        print(f"#{tc} {postfix_notation}")
        print(f"#{tc} {result}")
