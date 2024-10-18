import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    length = int(input())
    brackets = input()
    brace_check = True
    check_list = {')': '(', '}': '{', ']': '[', '>': '<'}
    open_brackets = []

    for bracket in brackets:
        if bracket in check_list.values():
            open_brackets.append(bracket)
        elif bracket in check_list:
            if open_brackets and open_brackets[-1] == check_list[bracket]:
                open_brackets.pop()
            else:
                brace_check = False
                break

    if open_brackets:
        brace_check = False

    print(f'#{tc} {int(brace_check)}')