import sys
import heapq

sys.stdin = open('input.txt')

'''for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))

    # 최소 힙과 최대 힙을 준비
    min_heap = boxes[:]
    max_heap = [-x for x in boxes]
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    for _ in range(N):
        min_val = heapq.heappop(min_heap)
        max_val = -heapq.heappop(max_heap)

        min_val += 1
        max_val -= 1

        heapq.heappush(min_heap, min_val)
        heapq.heappush(max_heap, -max_val)

    result = -heapq.heappop(max_heap) - heapq.heappop(min_heap)
    print(f'#{tc} {result}')

for tc in range(1, 11):
    number = int(input())
    arr = list(map(int, input().split()))

    # 상자를 이동하기 전에 정렬하여 높이를 재배열
    arr.sort()

    for _ in range(number):
        arr[0] += 1
        arr[-1] -= 1
        arr.sort()

    result = arr[-1] - arr[0]
    print(f'#{tc} {result}')'''


for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))

    upper_line = max(boxes)
    removed = 0

    while removed < N:
        for box in boxes:
            if box >= upper_line:
                removed += 1
        upper_line -= 1

    if removed > N:
        upper_line += 1

    filled = 0
    under_line = 0
    while filled < N:
        under_line += 1
        for box in boxes:
            if box < under_line:
                filled += 1

    if filled > N:
        under_line += 1
    print(N - removed, N - filled)
    print(f'#{tc}', upper_line - under_line)

'''import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))

    # 초기 설정
    upper_line = max(boxes)
    removed = 0

    # 상자 제거 작업
    while removed < N:
        for i in range(len(boxes)):
            if boxes[i] >= upper_line:
                boxes[i] -= 1
                removed += 1
                if removed == N:
                    break
        upper_line -= 1

    # 최종 상단 높이 조정
    if removed > N:
        upper_line += 1

    # 초기 설정
    filled = 0
    under_line = 0

    # 상자 채우기 작업
    while filled < N:
        under_line += 1
        for i in range(len(boxes)):
            if boxes[i] < under_line:
                boxes[i] += 1
                filled += 1
                if filled == N:
                    break

    # 최종 하단 높이 조정
    if filled > N:
        under_line += 1

    # 결과 출력
    print(f'#{tc} {upper_line - under_line}')'''

