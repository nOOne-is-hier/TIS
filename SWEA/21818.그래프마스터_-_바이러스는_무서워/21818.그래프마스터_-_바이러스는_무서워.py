import sys
sys.stdin = open('input.txt')

T = int(input())


def dfs_recur(start=1):
    copy_start = start
    for edge in two_way_edges:
        mother = edge[0]
        son = edge[1]
        if mother != copy_start or isinfested[son-1]:
            continue
        isinfested[son-1] = 1
        dfs_recur(son)


for tc in range(1, T + 1):

    num_vertex = int(input())
    num_edge = int(input())
    edges = [list(map(int, input().split())) for _ in range(num_edge)]
    two_way_edges = edges[:]
    for s, e in edges:
        two_way_edges += [[e, s]]
    isinfested = [0] * num_vertex
    isinfested[0] = 1
    dfs_recur()
    print(f'#{tc} {isinfested.count(1)-1}')
