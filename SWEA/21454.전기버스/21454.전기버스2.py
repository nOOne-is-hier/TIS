import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input().strip())

for tc in range(1, T + 1):
    K, N, M = map(int, input().strip().split())
    stops_with_station = list(map(int, input().strip().split()))

    # 충전소가 있는 정류장 표시
    station_index = [False] * (N + 1)
    for stop in stops_with_station:
        station_index[stop] = True

    # 현재 위치, 잔여 배터리, 충전 횟수 초기화
    position = 0
    cell = K
    charge_count = 0

    while position + K < N:
        # 충전 가능한 가장 먼 정류장 찾기
        next_position = position
        for i in range(position + 1, min(position + K + 1, N + 1)):
            if station_index[i]:
                next_position = i

        # 충전소가 없는 구간이면 도달 불가
        if next_position == position:
            charge_count = 0
            break

        # 다음 충전소로 이동 및 충전 횟수 증가
        position = next_position
        charge_count += 1

    # 결과 출력
    print(f'#{tc} {charge_count if position + K >= N else 0}')
