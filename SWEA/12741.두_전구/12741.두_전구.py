import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
result = deque()
for tc in range(1, T + 1):
    start1, end1, start2, end2 = map(int, input().split())

    '''    # 두 전구가 겹치지 않음
        if end1 < start2 or end2 < start1:
            result.append(f'#{tc}' + ' ' + '0')
    
        # 두 전구가 겹침
        if end1 >= start2 and end2 >= start1:
            overlapAmount = min(end2, end1) - max(start1, start2)
            result.append(f'#{tc}' + ' ' + f'{overlapAmount}')'''

    start = max(start1, start2)
    end = min(end1, end2)

    length = end - start
    if length < 1:
        result.append(f'#{tc}' + ' ' + '0')
    else:
        result.append(f'#{tc}' + ' ' + f'{length}')

print('\n'.join(result))