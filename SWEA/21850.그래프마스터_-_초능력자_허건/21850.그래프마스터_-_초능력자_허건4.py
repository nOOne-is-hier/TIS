import sys
import heapq

sys.stdin = open('input.txt')


def min_steps_v2(N, M):
    # 우선순위 큐 (비용, 현재 위치)
    pq = [(0, N)]
    visited = set()

    while pq:
        steps, current = heapq.heappop(pq)

        # 목표 위치에 도달했으면 종료
        if current == M:
            return steps

        # 이미 방문한 위치는 다시 처리하지 않음
        if current in visited:
            continue

        visited.add(current)

        # 이동 가능한 다음 위치 추가
        if current < M:
            heapq.heappush(pq, (steps + 1, current * 2))

        # +1 또는 -1 이동
        heapq.heappush(pq, (steps + 1, current + 1))
        if current > 0:
            heapq.heappush(pq, (steps + 1, current - 1))

    return -1  # 도달할 수 없는 경우 (여기서는 발생하지 않음)


for tc in range(1, int(input()) + 1):
    print(f'#{tc}', end=' ')
    N, M = list(map(int, input().split()))
    result = min_steps_v2(N, M)
    print(result)
