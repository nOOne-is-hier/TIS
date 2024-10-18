import sys
from collections import defaultdict
import heapq

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    print(f"#{tc}", end=' ')
    N, Q = map(int, input().split())
    # 병합처리를 위한 딕셔너리
    union = defaultdict(set)
    # 입력을 받을 리스트
    pond = []

    for idx in range(1, N + 1):
        n_start, n_end, _ = map(int, input().split())
        heapq.heappush(pond, (n_start, n_end, idx))

    # 병합 시작
    start_l, end_l, idx_l = heapq.heappop(pond)
    tag = 1
    union[tag].add(idx_l)
    while pond:
        start_r, end_r, idx_r = heapq.heappop(pond)
        if start_l <= end_r and end_l >= start_r:
            union[tag].add(idx_r)
            end_l = max(end_l, end_r)
        else:
            tag += 1
            union[tag].add(idx_r)
            start_l = start_r
            end_l = end_r

    # 쿼리 처리
    for _ in range(Q):
        bar1, bar2 = map(int, input().split())
        for bar in union:
            if bar1 in union[bar]:
                if bar2 in union[bar]:
                    print(1, end=' ')
                    break
                else:
                    print(0, end=' ')
                    break
            elif bar2 in union[bar]:
                if bar1 in union[bar]:
                    print(1, end=' ')
                    break
                else:
                    print(0, end=' ')
                    break
            else:
                print(0, end=' ')
    print()
