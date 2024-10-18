import sys
sys.stdin = open('input.txt')


def DFS(num_used=0, right=0, left=0, used=None, memo=None):
    # 각 추의 방문처리
    if used is None:
        used = [0] * N
    # 각 분기의 결과를 저장할 딕셔너리
    if memo is None:
        memo = {}
    # 방문한 경우라면 결과 변수에 경우의 수 합산
    if (num_used, right, left, tuple(used)) in memo:
        return memo[(num_used, right, left, tuple(used))]
    # 모든 추를 사용했다면 종료
    if num_used == N:
        return 1
    # 결과 값
    cases = 0
    # 순열에 대해 탐색
    for idx in range(N):
        if not used[idx]:
            used[idx] = 1
            # 왼쪽에 적재
            cases += DFS(num_used+1, right, left+weights[idx], used, memo)
            # 검증 후 오른쪽에 적재
            if left >= right + weights[idx]:
                cases += DFS(num_used+1, right + weights[idx], left, used, memo)
            used[idx] = 0 # 백트래킹
    # 현재의 상태 저장
    memo[(num_used, right, left, tuple(used))] = cases
    return cases

for tc in range(1, int(input()) + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    print(f'#{tc} {DFS()}')
