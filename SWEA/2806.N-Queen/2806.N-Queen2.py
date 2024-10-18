import sys
sys.stdin = open('input.txt')


def is_safe(n, r, c, unsafe_coordinates):
    copy_unsafe = set(unsafe_coordinates)
    temp_coordinates = set()

    for dir in range(8):
        dis = 1  # dis는 1로 시작해야 (r, c) 자리를 포함하지 않음
        while True:
            nr = r + (dr[dir] * dis)
            nc = c + (dc[dir] * dis)
            if 0 <= nr < n and 0 <= nc < n:
                temp_coordinates.add((nr, nc))
                dis += 1
            else:
                break

    copy_unsafe.update(temp_coordinates)
    return copy_unsafe

def dfs(n, row=0, n_queen=0, cases=None, unsafe_coordinates=None):
    if not cases:
        cases = [0]

    if not unsafe_coordinates:
        unsafe_coordinates = set()

    if n_queen == n:
        cases[0] += 1
        return

    for r in range(row, n):
        for c in range(n):
            if (r, c) not in unsafe_coordinates:
                new_unsafe_set = is_safe(n, r, c, unsafe_coordinates)
                dfs(n, r + 1, n_queen + 1, cases, new_unsafe_set)

    return cases[0]


for tc in range(1, int(input()) + 1):
    N = int(input())

    # 8 방향 정의 (위, 아래, 왼쪽, 오른쪽, 왼쪽 위 대각선, 오른쪽 위 대각선, 왼쪽 아래 대각선, 오른쪽 아래 대각선)
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    result = dfs(N)
    print(f'#{tc} {result}')
