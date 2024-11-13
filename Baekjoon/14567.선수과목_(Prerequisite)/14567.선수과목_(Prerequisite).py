import sys
from collections import deque, Counter
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
adjacency_list = [[] for _ in range(N)]
in_degrees = Counter()
result = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    adjacency_list[A].append(B)
    in_degrees[B] += 1
order = deque([])
for subject in range(N):
    if subject not in in_degrees:
        order.append(subject)
semesters = 1
while order:
    new_order = deque()

    while order:
        current_subject = order.popleft()
        result[current_subject] = semesters
        for pre_course in adjacency_list[current_subject]:
            in_degrees[pre_course] -= 1
            if in_degrees[pre_course] == 0:
                new_order.append(pre_course)

    semesters += 1
    order.extend(new_order)

print(*result)