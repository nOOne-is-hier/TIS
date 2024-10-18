# python 222,120KB 3,962ms
import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(500000)

def tree_traversal(node, last=-1):
    # 리프 노드인지 아닌지 확인
    is_leaf = True

    # 자식 노드의 early adapter 상태를 트래킹
    child_not_early_adapter = False

    # 자식 노드 순회
    for child in adjacency_list[node]:
        if child != last:
            is_leaf = False
            is_child_early = tree_traversal(child, node)
            if not is_child_early:
                # 자식이 early adapter가 아니면 현재 노드를 early adapter로 설정해야 할 가능성이 있음
                child_not_early_adapter = True

    if is_leaf:
        # 현재 노드가 리프인 경우
        return False

    if child_not_early_adapter:
        # 자식 중에 early adapter가 아닌 경우 현재 노드를 early adapter로 설정
        early_adapters.add(node)
        return True

    # 자식들이 모두 early adapter인 경우 현재 노드는 early adapter가 아님
    return False

N = int(input())
adjacency_list = [[] for _ in range(N)]

for _ in range(N - 1):
    parent, child = map(int, input().split())
    adjacency_list[parent - 1].append(child - 1)
    adjacency_list[child - 1].append(parent - 1)

early_adapters = set()
tree_traversal(0)
print(early_adapters)
print(len(early_adapters))
