import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())

    orders = [0] * (N + 1)
    adjancency_list = [[] for _ in range(N + 1)]

    for _ in range(N):
        idx, token, *children = input().split()
        orders[int(idx)] = token
        if children:
            for child in children:
                adjancency_list[int(idx)].append(int(child))

    for idx in range(N, 0, -1):
        if orders[idx] == chr(43):
            orders[idx] = int(orders[adjancency_list[idx][0]]) + int(orders[adjancency_list[idx][1]])

        elif orders[idx] == chr(45):
            orders[idx] = int(orders[adjancency_list[idx][0]]) - int(orders[adjancency_list[idx][1]])

        elif orders[idx] == chr(42):
            orders[idx] = int(orders[adjancency_list[idx][0]]) * int(orders[adjancency_list[idx][1]])

        elif orders[idx] == chr(47):
            orders[idx] = int(orders[adjancency_list[idx][0]]) // int(orders[adjancency_list[idx][1]])

    print(f'#{tc} {orders[1]}')