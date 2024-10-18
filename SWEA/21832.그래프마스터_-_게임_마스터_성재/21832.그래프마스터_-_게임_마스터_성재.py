import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    print(f'#{tc}', end=' ')
    N, M, K = list(map(int, input().split()))
    adjacency_matrix = [[0]*N for _ in range(N)]

    for _ in range(M):
        r, c, cost = list(map(int, input().split()))
        adjacency_matrix[r][c] = cost

    dungeon_and_cost = [0] * N

    for r in range(N):
        for c in range(N):
            if adjacency_matrix[r][c]:
                dungeon_and_cost[c] = adjacency_matrix[r][c]
                dungeon_and_cost[c] += dungeon_and_cost[r]

    for idx in range(N):
        if 0 < dungeon_and_cost[idx] <= K:
            print(idx, end=' ')

    print()