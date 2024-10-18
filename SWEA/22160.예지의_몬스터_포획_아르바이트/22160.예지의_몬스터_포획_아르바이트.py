import sys
from collections import OrderedDict
sys.stdin = open('input.txt')


def DFS(current_point=0, current_time=0, captured_monsters=None, visited_clients=None, min_time=None):
    # 결과 값
    if not min_time:
        min_time = [float('inf')]
    # 기저 조건을 위한 set
    if not captured_monsters:
        captured_monsters = set()
    if not visited_clients:
        visited_clients = set()
    # 백트래킹 조건: 현재 시간이 최소 시간보다 크면 더 이상 탐색하지 않음
    if current_time >= min_time[0]:
        return
    # 기저 조건
    if len(captured_monsters) == quests // 2 and len(visited_clients) == quests // 2:
        if min_time[0] > current_time:
            min_time[0] = current_time
            return

    # 몬스터 부터 포획
    for monster in range(1, quests // 2 + 1):
        if monster not in captured_monsters:
            captured_monsters.add(monster)
            DFS(monster, current_time + dist_table[current_point][monster], captured_monsters, visited_clients, min_time)
            captured_monsters.remove(monster)

    # 몬스터를 포획했다면 의뢰인 방문
    for client in range(-quests // 2, 0):
        if -client in captured_monsters and not client in visited_clients:
            visited_clients.add(client)
            DFS(client, current_time + dist_table[current_point][client], captured_monsters, visited_clients, min_time)
            visited_clients.remove(client)

    return min_time[0]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    village = [list(map(int, input().split())) for _ in range(N)]
    # 맵 마커
    marker = OrderedDict()
    # 시작점
    marker[0] = (0, 0)
    quests = 0
    # 퀘스트의 수
    for r in range(N):
        for c in range(N):
            if village[r][c]:
                quests += 1
                marker[village[r][c]] = (r, c)
    # 비용을 저장
    dist_table = [[200] * (quests + 1) for _ in range(quests + 1)]

    for mark1 in marker:
        for mark2 in marker:
            if mark1 != mark2:
                dist_table[mark1][mark2] = abs(marker[mark1][0]-marker[mark2][0]) + abs(marker[mark1][1]-marker[mark2][1])

    # 방문 시작
    result = DFS()

    print(f'#{tc}', result)