import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    snowBrothers = [list(map(int, input().split())) for _ in range(N)]
    # 발판들을 탐색
    blocks = []
    # 큐에 각 행의 0번째 열을 미리 넣어 놓음
    orders = deque([(row, 0) for row in range(N)])
    # 블록 탐색 시작
    while orders:
        row, column = orders.popleft()

        # 그리드 범위를 벗어나면 스킵
        if column >= M:
            continue

        # 숫자가 0이 아닌 블록을 만나면 오른쪽으로 탐색
        if snowBrothers[row][column] != 0:
            start_column = column
            end_column = column
            max_number = snowBrothers[row][column]

            # 오른쪽으로 이동하며 같은 숫자 블록을 찾음
            while end_column + 1 < M and snowBrothers[row][end_column + 1] in [1, 2, 3]:
                if max_number < snowBrothers[row][end_column + 1]:
                    max_number = snowBrothers[row][end_column + 1]
                end_column += 1

            # 블록 정보 저장 (숫자, 시작 열, 끝 열, 행값(높이))
            blocks.append((start_column, end_column, row, max_number))

            # 숫자 2가 포함된 블록은 시작 블록으로
            if max_number == 2:
                start_block_idx = len(blocks) - 1
            # 숫자 3이 포함된 블록은 도착 블록으로
            elif max_number == 3:
                end_block_idx = len(blocks) - 1

            # 다음 좌표로 이동 (다음 열)
            next_column = end_column + 1
            if next_column < M:
                orders.append((row, next_column))
        # 계속 탐색 (다음 열)
        else:
            next_column = column + 1
            if next_column < M:
                orders.append((row, next_column))

    # 블록 수
    num_blocks = len(blocks)

    # 인접 리스트 생성
    adjacency_list = [[] for _ in range(num_blocks)]

    # 블록간 연결 확인
    for idx in range(num_blocks):
        start_col1, end_col1, row1, num1 = blocks[idx]

        for cursor in range(idx + 1, num_blocks):
            start_col2, end_col2, row2, num2 = blocks[cursor]

            # 두 블록이 수직 이동 가능하다면 (X축 범위가 겹치는지 확인)
            if not (end_col1 < start_col2 or end_col2 < start_col1):
                # Y축 차이가 가중치 (수직 이동 거리)
                weight = abs(row1 - row2)
                adjacency_list[idx].append((cursor, weight))
                adjacency_list[cursor].append((idx, weight))

    # 가중치 제한이 있는 BFS 탐색
    limit = 1

    while True:
        orders = deque([start_block_idx])
        is_visited = [0] * num_blocks
        is_visited[start_block_idx] = 1     # 시작 노드 방문처리

        found = False   # 보석에 도달했는가

        while orders:
            idx = orders.popleft()

            if idx == end_block_idx:
                found = True
                break

            for next_node, weight in adjacency_list[idx]:
                if weight <= limit and not is_visited[next_node]:
                    is_visited[next_node] = 1
                    orders.append(next_node)
        # 보석을 먹었다면 loop 종료
        if found:
            break
        # 아니라면 limit 1 증가
        limit += 1

    print(f'#{tc}', limit)