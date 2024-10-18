import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    S, D = list(map(int, input().split()))

    queue = [[S, 0]]
    is_visited = [0]*100001
    is_visited[S] = 1

    while queue:
        current, cnt = queue.pop(0)
        if current == D:
            break

        next_position = [current//2, current * 2, current + 1, current - 1]

        for nxt in next_position:
            if 0 <= nxt <= 100000 and not is_visited[nxt]:
                is_visited[nxt] = 1
                queue.append([nxt, cnt + 1])

    print(f'#{tc} {cnt}')

