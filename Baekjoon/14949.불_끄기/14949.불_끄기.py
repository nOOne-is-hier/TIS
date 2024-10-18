import sys

sys.stdin = open('input.txt')

# 델타 배열 / 본, 상, 하, 좌, 우
dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]

# 스위치를 눌러서 생기는 상태 변화
def toggle_switch(row, columns, current_state):
    new_state = [line[:] for line in current_state]
    # 현재 행의 각 스위치에 대해
    for col in range(10):
        if columns & (1 << col): # 해당 스위치의 bit가 켜져 있는가?
            for direction in range(5):
                nr = row + dr[direction]
                nc = col + dc[direction]
                if 0 <= nr < 10 and 0 <= nc < 10:
                    new_state[nr][nc] = not new_state[nr][nc]   # 상태 전환

    return new_state

# 입력 처리
lights = [[False if light == '#' else True for light in input().strip()] for _ in range(10)]

# 최소 스위치 누름 횟수 추적 변수
min_switch_count = float('INF')

# 첫 행의 2^10가지 경우 모두 탐색
for first_row_cases in range(1 << 10):
    current_state = toggle_switch(0, first_row_cases, lights)

    # 스위치 누름 횟수 기록
    switch_count = bin(first_row_cases).count('1')

    # 두 번째 행부터 마지막 행까지 처리
    is_valid = True
    for row in range(1, 10):
        next_state = 0
        for col in range(10):
            if current_state[row - 1][col]: # 이전 행의 불을 끄는게 우선
                next_state |= (1 << col)

        current_state = toggle_switch(row, next_state, current_state)
        switch_count += bin(next_state).count('1')
            
        # 이전 행이 모두 꺼졌는지 확인
        if row < 9 and any(current_state[row - 1]):
            is_valid = not is_valid
            break


    # 마지막 두 행이 모두 꺼졌는지 확인
    if is_valid and not any(current_state[8]) and not any(current_state[9]):
        min_switch_count = min(min_switch_count, switch_count)

print(min_switch_count)