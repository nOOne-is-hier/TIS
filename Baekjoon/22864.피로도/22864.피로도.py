import sys
sys.stdin = open('input.txt')

A, B, C, M = map(int, input().split())

for time in range(24, -1, -1):  # 24시간부터 0시간까지 순회
    # 단 한 시간도 일할 수 없는 경우
    if A > M:
        print(0)
        break
    if A >= C:
        # 해당 케이스가 피로도 보다 같거나 작다면 종료, B 작업량은 무조건 양수
        if (A * time) - (C * (24 - time)) <= M:
            result = B * time
            print(result)
            break
    else:   # A가 C보다 작은경우
        fatigue = 0
        time = 0
        work_time = 0
        rest_time = 0
        while time < 24:
            time += 1
            if fatigue + A <= M:
                fatigue += A
                work_time += 1
            else:
                fatigue -= C
                if fatigue < 0:
                    fatigue = 0
                rest_time += 1
        result = B * work_time
        print(result)
        break