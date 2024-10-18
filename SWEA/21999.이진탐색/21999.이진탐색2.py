import sys

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())

    # 중위 순회에 따라 1부터 값 삽입
    inorder_traversal = []  # 방문한 노드를 저장할 리스트
    stack = []
    current = 1  # 루트 노드부터 시작

    while stack or current <= N:
        if current <= N:
            stack.append(current)
            current = current * 2  # 왼쪽 자식으로 이동
        else:
            current = stack.pop()
            inorder_traversal.append(current)  # 현재 노드를 방문
            current = current * 2 + 1

    print(f'#{tc} {inorder_traversal.index(1) + 1} {inorder_traversal.index(N//2) + 1}')