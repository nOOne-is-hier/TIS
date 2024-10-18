import sys
sys.stdin = open('input.txt')
from collections import deque


def is_related(adjacency_list=None):
    if not adjacency_list:
        adjacency_list = [[] for _ in range(4)]

    if magnetic1[2] != magnetic2[6]:
        adjacency_list[0].append(1)
        adjacency_list[1].append(0)
    if magnetic2[2] != magnetic3[6]:
        adjacency_list[1].append(2)
        adjacency_list[2].append(1)
    if magnetic3[2] != magnetic4[6]:
        adjacency_list[2].append(3)
        adjacency_list[3].append(2)

    return adjacency_list


def rotating(idx, direction, is_visited=None):
    if not is_visited:
        is_visited = [0] * 4
    is_visited[idx] = 1
    if idx == 0:
        if direction == 1:
            magnetic1.rotate(1)
        else:
            magnetic1.rotate(-1)
    elif idx == 1:
        if direction == 1:
            magnetic2.rotate(1)
        else:
            magnetic2.rotate(-1)
    elif idx == 2:
        if direction == 1:
            magnetic3.rotate(1)
        else:
            magnetic3.rotate(-1)
    elif idx == 3:
        if direction == 1:
            magnetic4.rotate(1)
        else:
            magnetic4.rotate(-1)
    # 좌우 자석 회전
    for other in adjacency_list[idx]:
        if not is_visited[other]:
            rotating(other, direction * -1, is_visited)

T = int(input())

for tc in range(1, T + 1):
    K = int(input())    # 회전 수
    magnetic1 = deque(list(map(int, input().split())))
    magnetic2 = deque(list(map(int, input().split())))
    magnetic3 = deque(list(map(int, input().split())))
    magnetic4 = deque(list(map(int, input().split())))

    # 자석의 맞물림을 담은 인접리스트
    for _ in range(K):
        adjacency_list = is_related()
        idx, direction = map(int, input().split())
        rotating(idx - 1, direction)

    result = magnetic1[0] + (magnetic2[0] * 2) + (magnetic3[0] * 4) + (magnetic4[0] * 8)
    print(f'#{tc}', result)