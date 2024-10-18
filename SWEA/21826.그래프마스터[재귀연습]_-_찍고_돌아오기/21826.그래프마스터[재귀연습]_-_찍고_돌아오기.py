import sys
sys.stdin = open('input.txt')

# 1. 반복문
'''array = ['start', 3, 1, 2, 1, 3, 2, 1, 2, 1, 'end']

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    to_return = []
    idx = n
    print(f'#{tc} {array[0]}', end=' ')
    while 0 < idx < len(array)-1:
        print(array[idx], end=' ')
        to_return.append(array[idx])
        idx += array[idx]
    print(array[-1], end=' ')
    for _ in range(len(to_return)):
        print(to_return.pop(), end=' ')
    print(array[0])'''

# 2. 재귀호출
'''array = [3, 1, 2, 1, 3, 2, 1, 2, 1]

T = int(input())


def jump_return(idx):
    if len(array)-1 < idx:
        print('end', end=' ')
        print(*to_return[::-1], end=' ')
        print('start')
        return

    print(array[idx], end=' ')
    to_return.append(array[idx])
    return jump_return(idx+array[idx])


for tc in range(1, T + 1):
    to_return = []
    print(f'#{tc} start', end=' ')
    idx = int(input())-1
    jump_return(idx)'''

# 3. 재귀호출
array = [3, 1, 2, 1, 3, 2, 1, 2, 1]

T = int(input())


def jump_return(idx, willReturn=False):
    if len(array)-1 < idx and not willReturn:
        print('end', end=' ')
        idx = to_return.pop()
        print(array[idx], end=' ')
        willReturn = True
        jump_return(idx, willReturn)
        return


    elif willReturn:
        if to_return:
            idx = to_return.pop()
            print(array[idx], end=' ')
            jump_return(idx, willReturn)
            return
        else:
            print('start')
            return

    print(array[idx], end=' ')
    to_return.append(idx)
    return jump_return(idx+array[idx], willReturn)


for tc in range(1, T + 1):
    to_return = []
    print(f'#{tc} start', end=' ')
    idx = int(input())-1
    jump_return(idx)