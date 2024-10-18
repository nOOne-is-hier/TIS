import sys
sys.stdin = open('input.txt')
from collections import deque

# 델타 배열 상, 하, 좌, 우
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 폭발 후 정렬하는 함수
def ordering_map(state):
    copy_state = [row[:] for row in state]  # 깊은 복사
    # 빈칸을 만나면 위의 값을 잡아 당김
    for r in range(1, H):
        for c in range(W):
            if not copy_state[r][c]:
                for nr in range(r, 0, -1):
                    copy_state[nr][c] = copy_state[nr - 1][c]
                copy_state[0][c] = 0
    return copy_state


# 완전 탐색
def DFS(remining_turns, current_state, current_blocks=None, min_score=None):
    # 남은 블록의 수를 저장
    if current_blocks is None:
        current_blocks = sum(sum(1 for block in row if block > 0) for row in current_state)
    # 기저 조건 1
    if current_blocks == 0:
        min_score[0] = 0
        return
    # 기저 조건 2
    if not remining_turns:
        min_score[0] = min(min_score[0], current_blocks)
        return
    # 결과를 저장할 리스트
    if not min_score:
        min_score = [current_blocks]

    # 탐색 시작
    for c in range(W):
        # 고유한 상태 저장
        copy_state = [row[:] for row in current_state]
        new_blocks = current_blocks

        # 첫 번째 투하 후 벽돌 충돌 확인
        target = next(((r, c) for r in range(H) if copy_state[r][c]), None)
        # 바닥까지 내려갔으면 해당 열 건너뛰기
        if target is None:
            continue
        # BFS를 위한 queue에 첫 번째 투하된 좌표 추가
        orders = deque([target])
        # BFS 연쇄 폭발 처리
        while orders:
            r, c = orders.popleft()
            if copy_state[r][c]:
                explode = copy_state[r][c]  # 폭발 반경
                copy_state[r][c] = 0    # 방문 처리
                new_blocks -= 1 # 폭발 카운트
                # 연쇄 폭발
                for dir in range(4):
                    for dis in range(1, explode):  # 폭발의 깊이
                        nr = r + (direction[dir][0] * dis)
                        nc = c + (direction[dir][1] * dis)
                        if 0 <= nr < H and 0 <= nc < W and copy_state[nr][nc]:
                            orders.append((nr, nc))
        # 폭발 종료 후 다음 차례로 이동
        new_state = ordering_map(copy_state)
        # 다음 단계 탐색
        DFS(remining_turns - 1, new_state, new_blocks, min_score)

    return min_score[0]


T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    breakBlocks = [list(map(int, input().split())) for _ in range(H)]

    result = DFS(N, breakBlocks)
    print(f'#{tc}', result)