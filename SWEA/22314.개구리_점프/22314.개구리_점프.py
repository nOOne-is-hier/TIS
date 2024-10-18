import sys
from collections import defaultdict

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    print(f"#{tc}", end=' ')
    N, Q = map(int, input().split())
    pond = defaultdict(set)

    for idx in range(1, N + 1):
        n_start, n_end, _ = map(int, input().split())
        merged = False  # 구간 병합 여부 플래그

        if pond:
            bars = list(pond.keys())
            for start, end in bars:
                # 겹치는 경우, 양쪽 방향 모두 처리하여 병합
                if n_start <= end and n_end >= start:
                    new_start = min(n_start, start)
                    new_end = max(n_end, end)
                    pond[(new_start, new_end)] = pond[(start, end)]  # 기존 구간 복사
                    pond[(new_start, new_end)].add(idx)  # 새로운 막대기 추가
                    del pond[(start, end)]  # 기존 구간 삭제
                    merged = True  # 병합된 구간임을 표시
                    break  # 한 번 병합했으면 중복되지 않도록 중단
        if not merged:
            # 병합이 안되었으면 새로운 구간 추가
            pond[(n_start, n_end)].add(idx)

    # 구간 및 막대기 출력
    print(pond)

    # 쿼리 처리
    for _ in range(Q):
        bar1, bar2 = map(int, input().split())
        found = False  # 막대기가 같은 구간에 있는지 여부
        for bar in pond:
            if bar1 in pond[bar] and bar2 in pond[bar]:
                print(1, end=' ')
                found = True
                break
        if not found:
            print(0, end=' ')
    print()
