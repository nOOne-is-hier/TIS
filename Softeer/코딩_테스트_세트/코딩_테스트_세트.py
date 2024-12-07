import sys

sys.stdin = open('input.txt')

import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)

    # ==============================
    # 입력 부분
    # ==============================
    N, T = map(int, sys.stdin.readline().split())

    for _ in range(T):
        # 각 시나리오의 문제 개수 입력 받기
        arr = list(map(int, sys.stdin.readline().split()))
        clist = []  # 정확히 i레벨인 문제 수
        dlist = []  # i레벨 또는 i+1레벨인 문제 수

        for i in range(len(arr)):
            if i % 2 == 0:
                clist.append(arr[i])
            else:
                dlist.append(arr[i])

        # ==============================
        # 이분 탐색을 위한 초기화
        # ==============================
        left = 0
        right = (sum(clist) + sum(dlist)) // N + 1  # 최대 가능한 세트 수
        ans = 0

        # ==============================
        # 이분 탐색 시작
        # ==============================
        while left <= right:
            mid = (left + right) // 2  # 현재 시도하는 세트 수 K

            if test(mid, N, clist, dlist):
                ans = mid  # 가능한 세트 수 업데이트
                left = mid + 1
            else:
                right = mid - 1

        # ==============================
        # 결과 출력
        # ==============================
        print(ans)

# ==============================
# 테스트 함수
# 각 레벨별로 K개의 문제를 확보할 수 있는지 확인
# ==============================
def test(K, N, clist, dlist):
    # ptable[i]: 레벨 i에서 사용할 수 있는 문제 수
    ptable = [0] * N
    ptable[0] = clist[0]  # 레벨 1의 정확한 난이도 문제 수

    for i in range(N - 1):
        if ptable[i] >= K:
            # 현재 레벨에서 필요한 문제 수를 충족한 경우
            # 다음 레벨로 애매한 문제 전부 넘김
            ptable[i + 1] = clist[i + 1] + dlist[i]
        elif ptable[i] + dlist[i] >= K:
            # 애매한 문제를 사용하여 현재 레벨의 필요한 문제 수를 충족
            used_d = K - ptable[i]  # 현재 레벨에서 사용한 애매한 문제 수
            remain_d = dlist[i] - used_d  # 다음 레벨로 넘길 애매한 문제 수
            ptable[i + 1] = clist[i + 1] + remain_d
        else:
            # 현재 레벨에서 필요한 문제 수를 충족할 수 없음
            return False

    # 마지막 레벨에서 필요한 문제 수 확인
    if ptable[N - 1] >= K:
        return True
    else:
        return False

threading.Thread(target=main).start()
