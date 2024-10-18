import random

N = 200
maze = [[1] * N for _ in range(N)]

# 랜덤한 시작점과 도착점 설정
start_r, start_c = random.randint(0, N-1), random.randint(0, N-1)
end_r, end_c = random.randint(0, N-1), random.randint(0, N-1)

maze[start_r][start_c] = 2
maze[end_r][end_c] = 3

# 경로를 생성하기 위한 간단한 랜덤화된 알고리즘
current_r, current_c = start_r, start_c
while (current_r, current_c) != (end_r, end_c):
    maze[current_r][current_c] = 0
    direction = random.choice(['up', 'down', 'left', 'right'])
    if direction == 'up' and current_r > 0:
        current_r -= 1
    elif direction == 'down' and current_r < N-1:
        current_r += 1
    elif direction == 'left' and current_c > 0:
        current_c -= 1
    elif direction == 'right' and current_c < N-1:
        current_c += 1

maze[current_r][current_c] = 3

# 파일로 저장
with open('input.txt', 'w') as f:
    f.write("1\n")  # 테스트 케이스의 수
    f.write(f"{N}\n")
    for row in maze:
        f.write(''.join(map(str, row)) + '\n')
