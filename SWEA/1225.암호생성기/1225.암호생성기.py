import sys
sys.stdin = open('input.txt')

# 1. 리스트의 메서드 사용
'''for _ in range(10):
    print(f'#{input()}', end=' ')
    encoded = list(map(int, input().split()))

    subtrahends = [1, 2, 3, 4, 5]
    idx = 0

    while encoded[-1] > 0:
        encoded.append(encoded.pop(0)-subtrahends[idx % 5])
        idx += 1

    encoded[-1] = 0

    print(*encoded)'''

# 2. deque사용
from collections import deque

for _ in range(10):
    print(f'#{input()}', end=' ')
    encoded = deque(list(map(int, input().split())))

    subtrahend = 0

    while encoded[-1] > 0:
        encoded.append(encoded.popleft()-((subtrahend % 5) + 1))
        subtrahend += 1

    encoded[-1] = 0

    print(*encoded)