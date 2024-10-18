import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    length = int(input())
    brackets = input()
    brace_check = True
    open_brackets = []
    top = -1

    for bracket in brackets:
        if bracket in '({[<':
            open_brackets.append(bracket)
            top += 1

        elif bracket == ')':
            if top >= 0 and open_brackets[top] == '(':
                open_brackets.pop()
                top -= 1
            else:
                brace_check = False
                break

        elif bracket == '}':
            if top >= 0 and open_brackets[top] == '{':
                open_brackets.pop()
                top -= 1
            else:
                brace_check = False
                break

        elif bracket == ']':
            if top >= 0 and open_brackets[top] == '[':
                open_brackets.pop()
                top -= 1
            else:
                brace_check = False
                break

        elif bracket == '>':
            if top >= 0 and open_brackets[top] == '<':
                open_brackets.pop()
                top -= 1
            else:
                brace_check = False
                break
    if open_brackets:
        brace_check = False

    print(f'#{tc} {int(brace_check)}')