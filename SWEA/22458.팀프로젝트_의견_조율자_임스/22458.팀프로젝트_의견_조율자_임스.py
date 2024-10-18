import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # A와 B의 의견을 집합으로 수집
    A_opinions = set()

    for _ in range(N):
        A_opinions.add(input().strip())

    result = set()
    for _ in range(M):
        tmp = input().strip()
        if tmp in A_opinions:
            result.add(tmp)

    # 교집합 결과 출력
    if not result:
        print(f'#{tc} NO!!')
    else:
        print(f'#{tc}',' '.join(sorted(result)))
