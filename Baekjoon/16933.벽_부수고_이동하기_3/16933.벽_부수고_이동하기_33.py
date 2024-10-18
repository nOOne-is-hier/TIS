import sys

sys.stdin = open('input.txt')

R, C, K = map(int, input().split())
M = [3] * (C + 2) + sum([[3] + list(map(int, (input().strip()))) + [3] for i in range(R)], []) + [3] * (C + 2)
C += 2
F = (R + 1) * (C)

visited = [999] * (C)
for i in range(R):
    visited += [999] + [0] * (C - 2) + [999]
visited += [999] * (C)
visited[C + 1] = 2
que = [(C + 1, K + 1)]
turn = 1
day = False
while visited[F - 2] == 0 and que:
    day = not day
    nq = []
    for p, m in que:  # 포지션과 망치

        if visited[p - 1] < m and (day or M[p - 1] == 0):
            visited[p - 1] = m
            nq.append((p - 1, m - M[p - 1]))
        if visited[p + 1] < m and (day or M[p + 1] == 0):
            visited[p + 1] = m
            nq.append((p + 1, m - M[p + 1]))
        if visited[p - C] < m and (day or M[p - C] == 0):
            visited[p - C] = m
            nq.append((p - C, m - M[p - C]))
        if visited[p + C] < m and (day or M[p + C] == 0):
            visited[p + C] = m
            nq.append((p + C, m - M[p + C]))
        if not day:
            nq.append((p, m))

    turn += 1
    que = nq

if visited[F - 2] == 0:
    print(-1)
else:
    print(turn)
