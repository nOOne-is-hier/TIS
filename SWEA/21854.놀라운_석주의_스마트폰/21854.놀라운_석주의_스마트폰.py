import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')

    Air_View_1 = list(map(int, input().split()))
    Air_View_2 = list(map(int, input().split()))

    if Air_View_1[2] < Air_View_2[0] or Air_View_2[2] < Air_View_1[0]:
        if Air_View_1[3] < Air_View_2[1] or Air_View_2[3] < Air_View_1[1]:
            print(4)

    elif Air_View_1[2:] == Air_View_2[:2] or Air_View_2[2:] == Air_View_1[:2]:
        print(3)

    elif Air_View_1[2] == Air_View_2[0] or Air_View_2[2] == Air_View_1[0] \
            or Air_View_1[3] == Air_View_2[1] or Air_View_2[3] == Air_View_1[1]:
        print(2)

    else:
        print(1)
