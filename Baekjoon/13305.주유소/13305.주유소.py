import sys
sys.stdin = open('input.txt')

N = int(input())    # 도시의 개수
# 시작점에서 해당 도시까지의 거리
distance_between_city = list(map(int, input().split()))
# 각 마을의 기름 값
oil_price = list(map(int, input().split()))

# 최소 비용 탐색 시작
last_min_cost = oil_price[0]
total_cost = last_min_cost * distance_between_city[0]
for idx in range(1, N - 1):
    if oil_price[idx] < oil_price[idx - 1]:
        last_min_cost = oil_price[idx]
    total_cost += last_min_cost * distance_between_city[idx]

print(total_cost)