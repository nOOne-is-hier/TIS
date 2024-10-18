import sys
sys.stdin = open('input.txt')


def DFS(row, column, current):
    # 기저조건
    if len(current) == 7:
        return {current}
    # 메모이제이션
    if (row, column, current) in memo:
        return memo[(row, column, current)]
    # 델타 배열
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 결과 저장
    unique_strings = set()
    # 탐색 시작
    for dir in range(4):
        nr = row + dr[dir]
        nc = column + dc[dir]
        if 0 <= nr < 4  and 0 <= nc < 4:
            unique_strings |= DFS(nr, nc, current + grid[nr][nc])
    # 상태 저장
    memo[(row, column, current)] = unique_strings
    return unique_strings


T = int(input())

for tc in range(1, T + 1):
    grid = [input().split() for _ in range(4)]
    memo = {}

    result = set()
    for r in range(4):
        for c in range(4):
            result |= DFS(r, c, grid[r][c])

    print(f'#{tc}', len(result))