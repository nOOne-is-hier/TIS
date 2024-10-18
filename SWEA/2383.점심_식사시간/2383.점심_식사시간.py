import sys
sys.stdin = open('input.txt')


def calculate_total_time(stair_group):
    if not stair_group:
        return 0
    # 계단에 최대 세 명만 있을 수 있음
    max_stair_present = 3
    # 리스트 정렬(오름차순)
    stair_group = sorted(stair_group, key=lambda x: x[0])
    # 총 시간
    total_times = []

    for idx, person in enumerate(stair_group):
        move_time, stair_time = person
        # 네 번째 부터 검증
        if idx >= max_stair_present:
            wait_time = total_times[idx - max_stair_present] - move_time
            wait_time = max(wait_time, 0)
            if wait_time > 0:
                total_times.append(move_time + stair_time + wait_time)  # 상쇄됨
            else:
                total_times.append(move_time + stair_time + 1)  # 1초 추가
        else:
            total_times.append(move_time + stair_time + 1)
            
    # 가장 큰 시간을 반환
    return max(total_times)


def DFS(idx=0, min_time=None, stair1=None, stair2=None):

    # 최소 시간
    if not min_time:
        min_time = [1000]
    # 경우의 수 저장
    if not stair1:
        stair1 = []
    if not stair2:
        stair2 = []
    # base condition
    if idx == numbers:
        current_time = max(calculate_total_time(stair1), calculate_total_time(stair2))
        min_time[0] = min(min_time[0], current_time)
        return
    # 차례 대로 두 개씩 뽑으면서 탐색
    stair1.append(weights[idx][0])
    DFS(idx + 1, min_time, stair1, stair2)
    stair1.pop()

    stair2.append(weights[idx][1])
    DFS(idx + 1, min_time, stair1, stair2)
    stair2.pop()

    return min_time[0]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    # 데이터 가공
    people = []
    exits = []
    for r in range(N):
        for c in range(N):
            if room[r][c] == 1:
                people.append((r, c))
            elif room[r][c] > 1:
                exits.append((r, c, room[r][c]))
    # 각 출구에 대한 weight 탐색
    numbers = len(people)
    weights = [[] for _ in range(numbers)]

    for idx, (pr, pc) in enumerate(people):
        for er, ec, level in exits:
            manhattan_distance = abs(pr - er) + abs(pc - ec)
            weights[idx].append((manhattan_distance, level))
    # brute force
    result = DFS()
    print(f'#{tc}', result)