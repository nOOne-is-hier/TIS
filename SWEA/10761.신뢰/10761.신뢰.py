import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')

    num_order, *order = input().split()

    # 명령 수행
    B_last = [['B', 1]]
    O_last = [['O', 1]]
    B_use_time = 0
    O_use_time = 0

    for idx in range(0, int(num_order)*2, 2):
        if order[idx] == 'B':
            B_last.append([order[idx], order[idx+1]])
            B_use_time += abs(int(B_last.pop(0)[1])-int(order[idx+1])) + 1
            if B_use_time <= O_use_time:
                B_use_time = O_use_time + 1

        else:
            O_last.append([order[idx], order[idx+1]])
            O_use_time += abs(int(O_last.pop(0)[1])-int(order[idx+1])) + 1
            if O_use_time <= B_use_time:
                O_use_time = B_use_time + 1

    print(max(B_use_time, O_use_time))