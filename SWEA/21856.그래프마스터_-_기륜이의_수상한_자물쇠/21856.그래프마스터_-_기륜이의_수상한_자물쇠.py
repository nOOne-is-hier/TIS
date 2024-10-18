import sys
sys.stdin = open('input.txt')
from collections import deque

def nomalization(pwd):
    if len(pwd) < 4:
        return ('0'*(4-len(pwd))) + pwd
    else:
        return pwd

def Double(pwd):
    return nomalization(str(int(pwd)*2%10000))

def Subtract(pwd):
    if pwd == '0000':
        return '9999'
    else:
        return nomalization(str(int(pwd) - 1))

def Left_rotate(pwd):
    return pwd[1:] + pwd[0]

def Right_rotate(pwd):
    return pwd[-1] + pwd[:3]


for tc in range(1, int(input()) + 1):
    start, goal = input().split()
    
    # 비밀먼호 정렬
    start = nomalization(start)
    goal = nomalization(goal)

    queue = deque([(start, '')])

    while queue:
        current, history = queue.popleft()
        if current == goal:
            print(f'#{tc} {history}')
            break

        next_tries = [(Double(current), 'D'), (Subtract(current), 'S'),
                      (Left_rotate(current), 'L'), (Right_rotate(current), 'R')]

        for trying in next_tries:
            queue.append((trying[0], history+trying[1]))