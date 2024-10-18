from array import array

class LinkedListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Graph:
    def __init__(self, N):
        self.heads = array('L', [0] * N)
        self.nodes = []
        for i in range(N):
            self.nodes.append(None)

    def connect(self, u, v):
        # 연결 리스트 방식으로 u -> v 연결
        self.nodes[u] = LinkedListNode(v, self.nodes[u])
        # 연결 리스트 방식으로 v -> u 연결 (양방향)
        self.nodes[v] = LinkedListNode(u, self.nodes[v])

def dfs(graph, node, parent, dp):
    dp[node][0] = 0  # 이 노드를 얼리 아답터로 선택하지 않은 경우
    dp[node][1] = 1  # 이 노드를 얼리 아답터로 선택한 경우

    current = graph.nodes[node]
    while current:
        child = current.data
        if child != parent:
            dfs(graph, child, node, dp)
            # 자식을 얼리 아답터로 선택하지 않은 경우는 부모는 반드시 얼리 아답터여야 함
            dp[node][0] += dp[child][1]
            # 자식을 얼리 아답터로 선택할 수도 있고 안 할 수도 있는 경우 중 최소값을 선택
            dp[node][1] += min(dp[child][0], dp[child][1])
        current = current.next

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    N = int(data[0])
    g = Graph(N)
    for i in range(1, N):
        u, v = map(int, data[i].split())
        u -= 1
        v -= 1
        g.connect(u, v)

    dp = [[0, 0] for _ in range(N)]  # dp[i][0]: i를 얼리 아답터로 선택 안 함, dp[i][1]: i를 얼리 아답터로 선택
    dfs(g, 0, -1, dp)

    # 루트 노드에서 얼리 아답터 수의 최소값 출력
    sys.stdout.write(f"{min(dp[0][0], dp[0][1])}\n")

if __name__ == "__main__":
    main()