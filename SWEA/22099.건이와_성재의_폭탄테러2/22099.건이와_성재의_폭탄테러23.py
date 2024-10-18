import sys
sys.stdin = open('input.txt')

import heapq

for tc in range(1, int(input()) + 1):
    bombs = []
    N = int(input())
    is_exploded = [0] * (N ** 2)

    idx = -1
    for _ in range(N):
        for num in map(int, input().split()):
            idx += 1
            heapq.heappush(bombs, (num, idx))

    # 델타 배열
    d_idx = [1, N, -1, -N]

    while bombs:
        current, idx = heapq.heappop(bombs)

        if not is_exploded[idx]:
            last_explode = current
            is_exploded[idx] = 1

            for dir in range(4):
                n_idx = idx + d_idx[dir]
                if 0 <= n_idx < N ** 2:
                    if any(dir == x for x in (0, 2)) and idx // N == n_idx // N:
                        is_exploded[n_idx] = 1
                    else:
                        is_exploded[n_idx] = 1


    print(f'#{tc} {last_explode}초')