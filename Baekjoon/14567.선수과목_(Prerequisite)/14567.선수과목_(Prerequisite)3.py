import io
import os
import sys
from collections import deque


def main() -> None:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    N, M = map(int, input().split())

    in_degrees = [0] * N
    adjacency_list = [[] for _ in range(N)]

    for _ in range(M):
        A, B = map(lambda x: int(x) - 1, input().split())
        adjacency_list[A].append(B)
        in_degrees[B] += 1

    visit_time = [0] * N
    queue = deque(i for i in range(N) if in_degrees[i] == 0)
    for i in queue:
        visit_time[i] = 1

    while queue:
        current_subject = queue.popleft()
        current_semester = visit_time[current_subject]

        for next_subject in adjacency_list[current_subject]:
            in_degrees[next_subject] -= 1
            if in_degrees[next_subject] == 0:
                queue.append(next_subject)
                visit_time[next_subject] = current_semester + 1

    print(" ".join(map(str, visit_time)))


sys.exit(main())
