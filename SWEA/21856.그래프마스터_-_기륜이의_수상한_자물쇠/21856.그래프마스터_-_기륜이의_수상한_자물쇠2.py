import sys
sys.stdin = open('input.txt')
from collections import deque

def Double(pwd):
    return pwd*2%10000

def Subtract(pwd):
    if not pwd:
        return 9999
    else:
        return pwd - 1

def Left_rotate(pwd):
    head = pwd//1000
    pwd *= 10
    pwd += head
    pwd -= head*10000
    return pwd

def Right_rotate(pwd):
    tail = int(str(pwd)[-1])
    pwd //= 10
    pwd += tail * 1000
    return pwd


for tc in range(1, int(input()) + 1):
    start, goal = map(int, input().split())
    is_visited = [0] * 10000
    is_visited[start] = 1
    queue = deque([(start, '')])

    while queue:
        current, history = queue.popleft()
        if current == goal:
            print(f'#{tc} {history}')
            break

        next_tries = [(Double(current), history+'D'), (Subtract(current), history+'S'),
                      (Left_rotate(current), history+'L'), (Right_rotate(current), history+'R')]

        for trying in next_tries:
            if not is_visited[trying[0]]:
                queue.append(trying)
                is_visited[trying[0]] = 1