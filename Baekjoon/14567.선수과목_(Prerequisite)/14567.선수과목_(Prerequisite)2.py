import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
adjacency_list = [[] for _ in range(N)]
in_degrees = [0] * N
result = [0] * N

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    adjacency_list[A].append(B)
    in_degrees[B] += 1

# 초기 진입 차수 0인 노드를 큐에 추가
order = deque([subject for subject in range(N) if in_degrees[subject] == 0])

semesters = 1
while order:
    for _ in range(len(order)):  # 현재 큐에 있는 노드들을 한 학기로 처리
        current_subject = order.popleft()
        result[current_subject] = semesters
        for pre_course in adjacency_list[current_subject]:
            in_degrees[pre_course] -= 1
            if in_degrees[pre_course] == 0:
                order.append(pre_course)

    semesters += 1

print(*result)
