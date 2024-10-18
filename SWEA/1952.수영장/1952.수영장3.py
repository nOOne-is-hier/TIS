import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    service_plans = list(map(int, input().split()))
    annual_plan = [0] + list(map(int, input().split()))
    # 메모이제이션
    memo_state = [0] * 13
    # 월별 탐색
    for month in range(1, 13):
        if month < 3:
            memo_state[month] = memo_state[month - 1] + min(service_plans[0] * annual_plan[month], service_plans[1])
        else:
            memo_state[month] = min(memo_state[month - 1] + min(service_plans[0] * annual_plan[month], service_plans[1]), memo_state[month - 3] + service_plans[2])
    result = min(memo_state[-1], service_plans[3])
    print(f'#{tc}', result)
