# python 315,852KB 5,428ms
import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(500000)

# 입력 처리
N = int(input())
adjacency_list = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

# DP 테이블: dp[x][0]은 x가 얼리 아답터가 아닐 때 최소 얼리 아답터 수
#           dp[x][1]은 x가 얼리 아답터일 때 최소 얼리 아답터 수
dp = [[0, 0] for _ in range(N + 1)]
visited = [False] * (N + 1)

def dfs(node):
    visited[node] = True
    dp[node][0] = 0  # 해당 노드가 얼리 아답터가 아닐 때
    dp[node][1] = 1  # 해당 노드가 얼리 아답터일 때

    for child in adjacency_list[node]:
        if not visited[child]:
            dfs(child)
            dp[node][0] += dp[child][1]  # 자식이 얼리 아답터일 때
            dp[node][1] += min(dp[child][0], dp[child][1])  # 자식이 얼리 아답터이거나 아니거나

dfs(1)
# 루트 노드가 얼리 아답터일 때와 아닐 때 중 최소 값을 출력
print(min(dp[1][0], dp[1][1]))
