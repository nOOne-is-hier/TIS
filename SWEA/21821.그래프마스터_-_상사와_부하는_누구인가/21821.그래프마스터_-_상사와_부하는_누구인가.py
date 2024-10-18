import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n = int(input())

    adjacency_matrix = [list(input().split()) for _ in range(n)]
    adjacency_list = []
    for r in range(n):
        for c in range(n):
            if adjacency_matrix[r][c] == '1':
                adjacency_list += [(r, c)]

    boss = []
    under = []

    for related in adjacency_list:
        if related[0] == 0:
            under.append(str(related[1]))
        elif related[1] == 0:
            boss.append((str(related[0])))

    print(f'#{tc} boss:{" ".join(boss)} / under:{" ".join(under)}')

