import sys
sys.stdin = open('input.txt')

def bfs(isvisited=None):
    if not isvisited:
        isvisited = [0] * N
        isvisited[0] = 1
    array = [0]

    while array:
        now = array.pop(0)
        print(now, end=' ')

        for idx in range(N):
            if adjacency_matrix[now][idx] == 0 or isvisited[idx]:
                continue

            isvisited[idx] = 1
            array.append(idx)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', end=' ')
    bfs(); print()