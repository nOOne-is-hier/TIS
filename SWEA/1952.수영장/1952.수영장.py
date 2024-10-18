import sys
sys.stdin = open('input.txt')


def daily_plan(current, state):
    copy_state = state[:]
    copy_state[current] = 1
    cost = annual_plan[current] * service_plans[0]
    return copy_state, cost

def monthly_plan(current, state):
    copy_state = state[:]
    copy_state[current] = 1
    cost = service_plans[1]
    return copy_state, cost

def quarterly_plan(current, state):
    copy_state = state[:]
    for next_month in range(3):
        if current + next_month <= 12:
            copy_state[current + next_month] = 1
    cost = service_plans[2]
    return copy_state, cost

def DFS(month=1, cost=0, min_cost=None, state=None):
    # 방문 처리
    if not state:
        state = [1] * 13
        for M in range(1, 13):
            if annual_plan[M]:
                state[M] = 0

    # 임시 최소값
    if not min_cost:
        min_cost = min([service_plans[3], service_plans[2] * 4, service_plans[1] * state.count(0),
                         service_plans[0] * sum(annual_plan)])
    # 기저 조건
    if month > 12:
        return min(min_cost, cost)

    # 각 월에 대해 정복하면서 진행
    if not state[month]:
        # 일일권
        state1, cost1 = daily_plan(month, state)
        min_cost = DFS(month + 1, cost + cost1, min_cost, state1)
        # 월간권
        state2, cost2 = monthly_plan(month, state)
        min_cost = DFS(month + 1, cost + cost2, min_cost, state2)
        # 분기권
        state3, cost3 = quarterly_plan(month, state)
        min_cost = DFS(month + 3, cost + cost3, min_cost, state3)
    else:
        min_cost = DFS(month + 1, cost, min_cost, state)

    return min_cost
            

T = int(input())

for tc in range(1, T + 1):
    service_plans = list(map(int, input().split()))
    annual_plan = [0] + list(map(int, input().split()))
    result = DFS()
    print(f'#{tc}', result)