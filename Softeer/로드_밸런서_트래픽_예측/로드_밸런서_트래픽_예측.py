import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import defaultdict, deque


# 트래픽 분배를 처리하는 함수
def distribute_traffic(N, K, server_info):
    # 각 서버로 들어오는 요청 수를 저장할 리스트
    requests = [0] * (N + 1)
    requests[1] = K  # 1번 서버는 루트 서버이므로 모든 요청이 처음에 여기로 들어옴
    print(requests)

    # 자식 노드 정보를 저장하는 딕셔너리
    children = defaultdict(list)
    for i in range(1, N + 1):
        info = server_info[i - 1]
        if info[0] > 0:  # 로드 밸런서일 경우
            for target in info[1:]:
                children[i].append(target)
    print(children)
    # 위상 정렬을 위한 준비
    indegree = [0] * (N + 1)
    for key in children:
        for child in children[key]:
            indegree[child] += 1
    print(indegree)
    # 위상 정렬을 위한 큐 초기화
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    print(queue)
    # 위상 정렬을 통해 트래픽 분배
    while queue:
        node = queue.popleft()
        if node in children:
            # 각 자식 노드로 트래픽을 분배
            num_children = len(children[node])
            base_traffic = requests[node] // num_children
            print(node, base_traffic)
            extra = requests[node] % num_children

            for i, child in enumerate(children[node]):
                requests[child] += base_traffic + (1 if i < extra else 0)
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

    return requests[1:]  # 1번 서버부터 N번 서버까지의 결과 반환


# 입력 처리
N, K = map(int, input().split())
server_info = []
for _ in range(N):
    data = list(map(int, input().split()))
    server_info.append(data)
print(server_info)
# 트래픽 분배 수행
result = distribute_traffic(N, K, server_info)

# 결과 출력
print(' '.join(map(str, result)))
