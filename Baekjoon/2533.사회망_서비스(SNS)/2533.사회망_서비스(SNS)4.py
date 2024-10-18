# python 388,352KB 4,732ms
# pypy 423,792KB 3,032ms

import sys
from collections import deque

sys.stdin = open('input.txt')

N = int(input())
adjacency_list = [set() for _ in range(N)]
parent_map = [-1] * N
for _ in range(N - 1):
    parent, child = map(int, input().split())
    adjacency_list[parent - 1].add(child - 1)
    adjacency_list[child - 1].add(parent - 1)

# 스택에 임의의 노드를 시작점으로 넣음 (트리이므로 어디서 시작해도 상관없음)
stack = deque([(0, -1)])  # (현재 노드, 부모 노드)
stack2 = deque()

# 첫 번째 순회: DFS로 노드를 방문하고 역순으로 저장
while stack:
    current, parent = stack.pop()
    stack2.append((current, parent))
    parent_map[current] = parent

    # 자식 노드 탐색
    for child in adjacency_list[current]:
        if child != parent:
            stack.append((child, current))

# 두 번째 순회: 리프 노드에서 부모로 돌아오면서 얼리 어답터 설정 및 트리 분해
while stack2:
    current, parent = stack2.pop()
    if parent != -1:
        # 현재 노드가 리프 노드인 경우, 부모 노드를 얼리 아답터로 설정하고 간선 제거
        adjacency_list[current].discard(parent)
        if adjacency_list[current]:
            for child in adjacency_list[current]:
                if child != parent:
                    if adjacency_list[child]:
                        break
            else:
                grandparent = parent_map[current]
                adjacency_list[grandparent].discard(current)

early_adopters = sum(1 if edges else 0 for edges in adjacency_list)
print(early_adopters)
