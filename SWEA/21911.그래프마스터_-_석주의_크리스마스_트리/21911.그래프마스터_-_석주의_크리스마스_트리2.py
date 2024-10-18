import sys
sys.stdin = open('input.txt')


def traversal(current=1):
    if current == -1:
        return

    inorder_traversal.append(current)
    traversal(adjacency_list[current - 1][0])
    preorder_traversal.append(current)
    traversal(adjacency_list[current - 1][1])
    postorder_traversal.append(current)


for tc in range(1, int(input()) + 1):
    print(f'#{tc}')
    N = int(input())
    adjacency_list = [[] for _ in range(N)]

    for _ in range(N):
        idx, *links = map(int, input().split())
        adjacency_list[idx - 1] = links

    preorder_traversal = []
    inorder_traversal = []
    postorder_traversal = []

    traversal()
    print(*preorder_traversal)
    print(*inorder_traversal)
    print(*postorder_traversal)