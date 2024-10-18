import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    num_vertex = int(input())
    num_edge = int(input())
    edges = [list(map(int, input().split())) for _ in range(num_edge)]
    adjacency_list = [[e if s == i else s for s, e in edges if s == i or e == i] for i in range(1, num_vertex + 1)]
    # [[2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

    idx = 0
    isinfested = [0] * num_vertex
    isinfested[0] = 1
    current_edges = [adjacency_list[0]]

    while current_edges:

        for next_vertex in current_edges[0]:
            if isinfested[next_vertex-1]:
                continue
            idx = next_vertex-1
            isinfested[idx] = 1
            current_edges.append(adjacency_list[idx])

        current_edges.pop(0)

    print(f'#{tc} {isinfested.count(1)-1}')

    '''edges = [[] for _ in range(num_vertex)]
    for _ in range(num_edge):
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)'''