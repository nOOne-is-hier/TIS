import sys
from collections import deque

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())

    binary_search_tree = [0] * (N + 1)

    # 중위 순회에 따라 1부터 값 삽입
    inorder_traversal = []
    is_visited = [0] * (N + 1)
    stack = deque([1])

    while stack:
        current = stack[-1]
        if is_visited[current]:
            inorder_traversal.append(stack.pop())
            if stack:
                right = stack[-1] * 2 + 1
                if right <= N:
                    inorder_traversal.append(stack.pop())
                    stack.append(right)
                    continue

        else:
            is_visited[current] = 1

        if current * 2 > N and stack:
            inorder_traversal.append(stack.pop())
            if stack:
                right = stack[-1] * 2 + 1
                if right <= N:
                    inorder_traversal.append(stack.pop())
                    stack.append(right)
                    continue

        elif not stack:
            break

        else:
            stack.append(current * 2)

    print(f'#{tc} {inorder_traversal.index(1) + 1} {inorder_traversal.index(N//2) + 1}')