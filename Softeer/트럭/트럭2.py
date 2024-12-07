import sys

sys.stdin = open('input.txt')

import sys
import bisect
import threading

def main():
    # 재귀 깊이 제한을 높여 입력 크기에 맞게 처리할 수 있도록 설정
    sys.setrecursionlimit(1 << 25)

    # 소비자 수 입력
    N = int(sys.stdin.readline())

    # 전체 제안을 저장할 리스트
    proposals = []
    # 소비자별 제안을 저장할 리스트 (N개의 빈 리스트)
    consumer_proposals = [[] for _ in range(N)]

    # 각 소비자의 제안 처리
    for i in range(N):
        arr = sys.stdin.readline().split()
        Ai = int(arr[0])  # 현재 소비자가 보낸 제안 수
        arr = arr[1:]  # 제안 데이터를 분리
        # 크기 리스트와 가격 리스트로 분리
        Si_list = list(map(int, arr[::2]))
        Pi_list = list(map(int, arr[1::2]))
        # 각 제안을 proposals와 consumer_proposals에 저장
        for Sij, Pij in zip(Si_list, Pi_list):
            proposals.append((Sij, Pij, i))  # 전체 제안 저장
            consumer_proposals[i].append((Sij, Pij))  # 소비자별 저장

    # 시나리오 수 입력
    M = int(sys.stdin.readline())
    # 목표 매출 입력
    Q_list = list(map(int, sys.stdin.readline().split()))

    # 1. 크기(Sij)를 기준으로 전체 제안 정렬
    proposals.sort()

    # 2. 고유한 크기 리스트 생성 (중복 제거 후 정렬)
    S_list = sorted(set([Sij for Sij, Pij, i in proposals]))

    # 3. 크기별 제안 그룹화
    from collections import defaultdict
    proposals_by_S = defaultdict(list)
    for Sij, Pij, i in proposals:
        proposals_by_S[Sij].append((i, Pij))

    # 4. 신차 크기별 매출 계산
    total_revenue = 0  # 총 매출 초기화
    current_best_P = [0] * N  # 각 소비자별로 선택된 최대 가격 초기화
    S_to_total_revenue = {}  # 크기별 총 매출 저장

    # 크기를 순차적으로 처리
    for S in S_list:
        # 해당 크기에서의 제안 처리
        for i, Pij in proposals_by_S[S]:
            # 더 좋은 조건의 제안이 있으면 업데이트
            if Pij > current_best_P[i]:
                total_revenue -= current_best_P[i]  # 이전 매출 제거
                current_best_P[i] = Pij  # 새로운 최대 가격 저장
                total_revenue += current_best_P[i]  # 새로운 매출 추가
        # 현재 크기에서의 총 매출 저장
        S_to_total_revenue[S] = total_revenue

    # 5. 이진 탐색 준비
    revenue_list = []  # 총 매출 리스트
    S_values = []  # 크기 리스트
    for S in sorted(S_to_total_revenue.keys()):
        total_revenue = S_to_total_revenue[S]
        revenue_list.append(total_revenue)  # 매출 추가
        S_values.append(S)  # 크기 추가

    # 6. 각 시나리오의 목표 매출에 대해 처리
    result = []
    for Qk in Q_list:
        if revenue_list[-1] < Qk:  # 목표 매출이 최대 매출을 초과하는 경우
            result.append(-1)  # -1 출력
        else:
            # 이진 탐색으로 목표 매출을 달성할 수 있는 최소 크기 찾기
            idx = bisect.bisect_left(revenue_list, Qk)
            result.append(S_values[idx])  # 해당 크기 추가

    # 결과 출력
    print(' '.join(map(str, result)))

# 멀티스레드로 실행 (빠른 입력 처리)
threading.Thread(target=main).start()
