import sys
sys.stdin = open('input.txt')


def solve():
    # 첫 줄은 테스트 케이스 수
    T = int(input())

    for tc in range(1, T + 1):
        results = [f"#{tc}"]

        # 통나무 수 N과 쿼리 수 Q 입력
        N, Q = map(int, input().split())

        # 병합 처리를 위한 딕셔너리
        union = {}

        # 통나무 구간 저장
        pond = [()] * (N + 1)
        for idx in range(1, N + 1):
            n_start, n_end, _ = map(int, input().split())  # y는 사용하지 않음
            pond[idx] = (n_start, n_end, idx)

        # 통나무의 시작점 기준으로 정렬
        pond.sort()

        # 병합 시작
        _, end_l, idx_l = pond[1]
        tag = 1
        union[idx_l] = tag
        for cursor in range(2, N + 1):
            start_r, end_r, idx_r = pond[cursor]
            if end_l >= start_r:
                union[idx_r] = tag
                end_l = max(end_l, end_r)
            else:
                tag += 1
                union[idx_r] = tag
                end_l = end_r

        # 쿼리 처리 및 출력
        for _ in range(Q):
            bar1, bar2 = map(int, input().split())
            if union[bar1] == union[bar2]:
                results.append("1")
            else:
                results.append("0")

        # 결과 출력
        print(" ".join(results))


# 메인 함수 호출
solve()