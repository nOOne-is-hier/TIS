import sys

sys.stdin = open('input.txt')

def main():  # 메인 함수를 정의합니다
    N = int(input())  # 소비자 수 N을 입력받습니다
    proposals = []  # 모든 제안을 저장할 리스트를 초기화합니다
    consumer_proposals = []  # 소비자별 제안을 저장할 리스트를 초기화합니다
    for i in range(N):  # 각 소비자에 대해 반복합니다
        arr = input().split()  # 'Ai Si1 Pi1 Si2 Pi2 ...' 형식의 입력을 받습니다
        Ai = int(arr[0])  # 현재 소비자의 제안 수 Ai를 가져옵니다
        arr = arr[1:]  # 나머지 부분(Si와 Pi 값들)을 가져옵니다
        consumer_proposals.append([])  # 현재 소비자의 제안 리스트를 초기화합니다
        for j in range(Ai):  # 소비자의 각 제안에 대해 반복합니다
            Sij = int(arr[2 * j])  # 이 제안의 최소 크기 Sij를 가져옵니다
            Pij = int(arr[2 * j + 1])  # 이 제안의 가격 Pij를 가져옵니다
            proposals.append((Sij, Pij, i))  # 제안을 전체 제안 리스트에 추가합니다
            consumer_proposals[i].append((Sij, Pij))  # 제안을 소비자의 제안 리스트에 추가합니다
    M = int(input())  # 시나리오 수 M을 입력받습니다
    Q_list = list(map(int, input().split()))  # 목표 매출 Qk들을 입력받습니다
    proposals.sort()  # 제안들을 크기 Sij 기준으로 정렬합니다
    S_set = set()  # 고유한 크기 S를 저장할 집합을 초기화합니다
    for Sij, Pij, i in proposals:  # 각 제안에 대해 반복합니다
        S_set.add(Sij)  # 크기 Sij를 집합에 추가합니다
        S_list = sorted(S_set)  # 고유한 크기 S를 정렬하여 리스트로 만듭니다
    proposals_by_S = {}  # 크기 Sij별로 제안을 그룹화할 사전을 초기화합니다
    for Sij, Pij, i in proposals:  # 각 제안에 대해 반복합니다
        if Sij not in proposals_by_S:  # Sij가 사전에 없으면
            proposals_by_S[Sij] = []  # 새로운 리스트를 만듭니다
        proposals_by_S[Sij].append((i, Pij))  # 제안을 해당 크기의 리스트에 추가합니다
    total_revenue = 0  # 총 매출을 0으로 초기화합니다
    revenue_list = []  # 각 크기별 총 매출을 저장할 리스트를 초기화합니다
    S_values = []  # 크기 S를 저장할 리스트를 초기화합니다
    current_best_P = [0] * N  # 각 소비자의 현재 최고의 제안을 0으로 초기화합니다
    for S in S_list:  # 각 크기 S에 대해 반복합니다
        for i, Pij in proposals_by_S[S]:  # 해당 크기의 각 제안에 대해 반복합니다
            if Pij > current_best_P[i]:  # 이 제안이 소비자 i의 현재 최고 제안보다 좋으면
                total_revenue -= current_best_P[i]  # 이전 제안을 총 매출에서 빼줍니다
                current_best_P[i] = Pij  # 소비자 i의 최고 제안을 업데이트합니다
                total_revenue += current_best_P[i]  # 새로운 제안을 총 매출에 더해줍니다
        revenue_list.append(total_revenue)  # 현재 총 매출을 리스트에 추가합니다
        S_values.append(S)  # 현재 크기 S를 리스트에 추가합니다
    result = []  # 결과를 저장할 리스트를 초기화합니다
    for Qk in Q_list:  # 각 목표 매출 Qk에 대해 반복합니다
        left = 0  # 이분 탐색의 왼쪽 포인터를 0으로 초기화합니다
        right = len(revenue_list) - 1  # 이분 탐색의 오른쪽 포인터를 설정합니다
        answer = -1  # 답을 -1로 초기화합니다 (찾을 수 없는 경우)
        while left <= right:  # 이분 탐색을 수행합니다
            mid = (left + right) // 2  # 중간 인덱스를 계산합니다
            if revenue_list[mid] >= Qk:  # 중간 매출이 목표 매출 이상이면
                answer = S_values[mid]  # 현재 크기를 답으로 설정합니다
                right = mid - 1  # 더 작은 크기를 찾아보기 위해 오른쪽 포인터를 이동합니다
            else:  # 중간 매출이 목표 매출보다 작으면
                left = mid + 1  # 더 큰 매출을 찾아보기 위해 왼쪽 포인터를 이동합니다
        result.append(answer)  # 찾은 답을 결과 리스트에 추가합니다
    print(' '.join(map(str, result)))  # 결과를 공백으로 구분하여 출력합니다

main()  # 메인 함수를 호출합니다
