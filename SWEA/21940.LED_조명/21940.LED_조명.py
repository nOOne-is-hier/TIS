import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    wished_state = [0] + input().split()
    
    # 결과 값
    click_switch = 0
    for idx in range(1, N + 1):
        if wished_state[idx] == '1':
            multiple = idx
            click_switch += 1
            while idx < N + 1:
                if wished_state[idx] == '1':
                    wished_state[idx] = '0'
                else:
                    wished_state[idx] = '1'
                idx += multiple

    print(f'#{tc} {click_switch}')