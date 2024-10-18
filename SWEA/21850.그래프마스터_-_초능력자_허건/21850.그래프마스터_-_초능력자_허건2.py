import sys
sys.stdin = open('input.txt')

from collections import deque


def bfs_min_steps(N, M):
    queue = deque([(N, 0)])
    visited = set()

    while queue:
        current, steps = queue.popleft()

        if current == M:
            return steps

        visited.add(current)

        # 다음 가능한 연산 추가
        next_steps = [current + 1, current - 1, current * 2]

        for next_step in next_steps:
            if next_step == M:
                return steps + 1
            if 0 <= next_step <= 100000 and next_step not in visited:
                queue.append((next_step, steps + 1))
                visited.add(next_step)

    return -1  # 목표값에 도달할 수 없는 경우


# 입력 예시
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    teleport_count = bfs_min_steps(N, M)
    print(f'#{tc} {teleport_count}')
