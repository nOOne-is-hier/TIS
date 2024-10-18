import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    stops_with_station = list(map(int, input().split()))

    # 충전소가 있는 정류장
    station_index = [False] * (N + 1)
    for stop in stops_with_station:
        station_index[stop] = True

    # 잔여 배터리
    cell = K
    # 충전 경고
    need_charge = False
    # 충전 횟수
    charge_count = 0
    # 완주 가능성
    arrived = True

    # 한 정류장 씩 이동
    for i in range(1, N):

        # 이동시 배터리 소모
        cell -= 1

        # 이동가능 범위 안에 충전소가 없으면 충전 경고
        if i < N - K and not station_index[i + cell]:
            need_charge = True

        # 남은 연료로 종점까지 갈 수 없으면 충전 경고
        elif i >= N - K and not i + cell >= N:
            need_charge = True
        
        # 연료가 0이 되면 충전 경고
        if not cell:
            need_charge = True

        # 충전 경고가 있고 해당 위치에 충전소가 있다면 충전
        if need_charge and station_index[i]:
            need_charge = False
            station_index[i] = False
            cell = K
            charge_count += 1

        # 종점이 아닌데 연료도 없고 충전소도 없을 때 실패
        if not cell and not station_index[i] and i != N-1:
            arrived = False
            break

    if arrived:
        print(f'#{tc}', charge_count)

    else:
        print(f'#{tc}', 0)

