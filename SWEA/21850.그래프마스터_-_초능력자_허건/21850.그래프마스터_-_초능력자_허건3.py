import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    print(f'#{tc}', end=' ')
    N, M = list(map(int, input().split()))

    if N >= M:
        print(N-M)
        continue


    else:
        queue = [[N, 0]]
        is_visited = [0]*100001
        is_visited[N] = 1
        while queue:
            current, cnt = queue.pop(0)
            if current == M:
                break

            tmps = [current + 1, current - 1, current * 2]

            for tmp in tmps:
                if 0<= tmp <= 100000 and not is_visited[tmp]:
                    is_visited[tmp] = 1
                    queue.append([tmp, cnt+1])

    print(cnt)


