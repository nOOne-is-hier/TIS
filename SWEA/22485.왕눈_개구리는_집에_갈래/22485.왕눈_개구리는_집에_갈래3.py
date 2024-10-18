import sys
from collections import deque
import heapq

sys.stdin = open('input.txt')

# 델타 배열: 좌측 아래, 아래, 우측 아래 방향
dr = [1, 1, 1]
dc = [-1, 0, 1]

T = int(input())

for tc in range(1, T + 1):
    # 입력 처리
    height, width = map(int, input().split())
    the_way_home = [list(map(int, input().split())) for _ in range(height)]

    # BFS를 위한 큐 초기화 (점수 없이)
    queue = deque([(0, 0)])  # (row, col)

    # 방문 기록 배열 (최대 점수를 갱신하기 위해 사용)
    max_scores = [[-float('inf')] * width for _ in range(height)]
    max_scores[0][0] = the_way_home[0][0]

    # 디버깅을 위한 큐 크기 추적
    max_queue_size_no_score = 0

    # BFS 탐색 시작 (점수 없이 큐에 저장)
    while queue:
        # 큐 크기 갱신
        max_queue_size_no_score = max(max_queue_size_no_score, len(queue))

        row, col = queue.popleft()
        current_score = max_scores[row][col]

        # 세 방향으로 이동
        for dir in range(3):
            nr = row + dr[dir]
            nc = col + dc[dir]

            # 유효한 위치인지 확인
            if 0 <= nr < height and 0 <= nc < width and the_way_home[nr][nc] != 0:
                new_score = current_score + the_way_home[nr][nc]

                # 더 높은 점수를 발견했을 때 갱신하고 큐에 추가
                if new_score > max_scores[nr][nc]:
                    max_scores[nr][nc] = new_score
                    queue.append((nr, nc))

    # 최하단 행에서 얻을 수 있는 최대 점수 찾기
    result_no_score = max(max_scores[height - 1])

    # 기존 방식: BFS (점수 포함해서 큐에 저장)
    queue = deque([(0, 0, the_way_home[0][0])])  # (row, col, current_score)
    max_scores = [[-float('inf')] * width for _ in range(height)]
    max_scores[0][0] = the_way_home[0][0]

    # 디버깅을 위한 큐 크기 추적
    max_queue_size_with_score = 0

    # BFS 탐색 시작 (점수 포함하여 큐에 저장)
    while queue:
        # 큐 크기 갱신
        max_queue_size_with_score = max(max_queue_size_with_score, len(queue))

        row, col, current_score = queue.popleft()

        # 세 방향으로 이동
        for dir in range(3):
            nr = row + dr[dir]
            nc = col + dc[dir]

            # 유효한 위치인지 확인
            if 0 <= nr < height and 0 <= nc < width and the_way_home[nr][nc] != 0:
                new_score = current_score + the_way_home[nr][nc]

                # 더 높은 점수를 발견했을 때 갱신하고 큐에 추가
                if new_score > max_scores[nr][nc]:
                    max_scores[nr][nc] = new_score
                    queue.append((nr, nc, new_score))

    # 최하단 행에서 얻을 수 있는 최대 점수 찾기
    result_with_score = max(max_scores[height - 1])

    # 결과 출력
    print(f'#{tc} (Without Score in Queue) {result_no_score}, Max queue size: {max_queue_size_no_score}')
    print(f'#{tc} (With Score in Queue) {result_with_score}, Max queue size: {max_queue_size_with_score}')