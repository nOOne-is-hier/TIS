import sys
sys.stdin = open('input.txt')

T = int(input())


def bfs(isvisited, start=0, case=[0]):

    if len(case) == 3:
        print(*case)
        return

    copy_case = case[:]

    idx = -1
    for c in adjacency_matrix[start]:
        idx += 1
        if c == 1 and not isvisited[idx]:
            copy_case.append(idx)
            isvisited[idx] = 1
            bfs(isvisited, idx, copy_case)
            copy_case.pop()

for tc in range(1, T + 1):
    N = int(input())
    adjacency_matrix = [list(map(int, input().split())) for _ in range(int(N))]
    check_vaild_array = [0] * N
    check_vaild_array[0] = 1
    print(f'#{tc}')
    bfs(check_vaild_array)
