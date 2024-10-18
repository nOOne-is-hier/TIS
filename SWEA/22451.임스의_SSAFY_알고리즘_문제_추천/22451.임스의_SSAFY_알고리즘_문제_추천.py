import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')

    N = int(input())
    problems_per_day = list(map(int, input().split()))
    M = int(input())
    queries = deque()
    for _ in range(M):
        language, grade, each = input().split()
        for _ in range(int(each)):
            queries.append((language, int(grade)))

    for problems in problems_per_day:
        solved = 0
        for _ in range(problems):
            language, grade = queries.popleft()
            if language == 'ko' and grade >= 3:
                solved += 1
        print(solved, end=' ')

    print()