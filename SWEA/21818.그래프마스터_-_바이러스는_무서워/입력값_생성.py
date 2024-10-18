import random
import sys

sys.stdout = open('input.txt', 'w')

# 정점의 수
num_vertex = 100
# 간선의 수를 적절하게 설정
num_edge = 50

# 1부터 num_vertex까지의 정점 생성
vertices = list(range(1, num_vertex + 1))

# 랜덤하게 간선 생성 (간선이 중복되지 않도록 set 사용)
edges = set()

while len(edges) < num_edge:
    # 두 개의 다른 정점을 무작위로 선택
    u = random.choice(vertices)
    v = random.choice(vertices)
    if u != v:
        edge = (u, v)
        edges.add(edge)

# 간선 리스트로 변환
edges = list(edges)

# 테스트 케이스 출력
print(f"{num_vertex}")
print(f"{len(edges)}")
for edge in edges:
    print(f"{edge[0]} {edge[1]}")
