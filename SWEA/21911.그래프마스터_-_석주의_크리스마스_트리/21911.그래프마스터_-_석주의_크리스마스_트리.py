import sys
sys.stdin = open('input.txt')

def pattern1(num):
    num -= 1
    if num == -2:
        return
    return pattern1(adjancency_list[num][0]), print(num + 1, end=' '), pattern1(adjancency_list[num][1])
def pattern2(num):
    if num == -2:
        return
    print(num + 1, end=' ')
    return pattern2(adjancency_list[num][0]-1), pattern2(adjancency_list[num][1]-1)

def pattern3(num):
    num -= 1
    if num == -2:
        return
    return pattern3(adjancency_list[num][0]), pattern3(adjancency_list[num][1]), print(num + 1, end=' ')

for tc in range(1, int(input()) + 1):
    print(f'#{tc}')
    N = int(input())
    adjancency_list = [[] for _ in range(N)]

    for _ in range(N):
        idx, *links = list(map(int, input().split()))
        adjancency_list[idx - 1] = links

    pattern1(1)
    print()
    pattern2(0)
    print()
    pattern3(1)
    print()