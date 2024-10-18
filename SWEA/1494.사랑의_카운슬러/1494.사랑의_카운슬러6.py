import sys

sys.stdin = open('input.txt')


def dfs(i, plus, minus, x, y, ans):
    if plus == M and minus == M:
        return min(x ** 2 + y ** 2, ans)
    if plus < M:
        ans = dfs(i + 1, plus + 1, minus, x + arr[i][0], y + arr[i][1], ans)
    if minus < M:
        ans = dfs(i + 1, plus, minus + 1, x - arr[i][0], y - arr[i][1], ans)
    return ans


for tc in range(1, int(input()) + 1):
    N = int(input())
    M = N // 2
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    ans = 2e12
    ans = dfs(0, 0, 0, 0, 0, ans)

    print(f'#{tc} {ans}')

'''
import sys

sys.stdin = open('input.txt')


def dfs(i, plus, minus, x, y, ans):
    # 모든 지렁이를 다 탐색한 경우 종료
    if i == N:
        if plus == M and minus == M:
            return min(x ** 2 + y ** 2, ans)
        return ans
    
    # 현재 상태가 최적해가 될 가능성이 없다면 가지치기
    if plus > M or minus > M:
        return ans

    # 현재 지렁이를 선택하는 경우
    if plus < M:
        ans = dfs(i + 1, plus + 1, minus, x + arr[i][0], y + arr[i][1], ans)
    
    # 현재 지렁이를 선택하지 않는 경우
    if minus < M:
        ans = dfs(i + 1, plus, minus + 1, x - arr[i][0], y - arr[i][1], ans)

    return ans


for tc in range(1, int(input()) + 1):
    N = int(input())
    M = N // 2
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    ans = 2e12
    ans = dfs(0, 0, 0, 0, 0, ans)

    print(f'#{tc} {ans}')

'''