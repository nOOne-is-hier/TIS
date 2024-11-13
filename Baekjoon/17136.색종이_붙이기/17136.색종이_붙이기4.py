import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 2진수로 변환하여 각 행을 하나의 정수로 저장
board = [int(input().replace(' ', ''), 2) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]  # 색종이 크기별 남은 개수 (0은 사용 안 함)
paper_count = 26  # 최대 25장 사용 가능 (최소값 갱신 위해 충분히 큰 값으로 초기화)


def checkcheck(lst, count, start_row):
    global paper_count

    # 이미 최적 결과를 초과하면 가지치기
    if count >= paper_count:
        return

    # 모든 셀이 0이면 최소 종이 개수를 갱신
    if not any(lst):
        paper_count = min(paper_count, count)
        return

    # 행과 열을 순회하면서 색종이 놓기
    for r in range(start_row, 10):
        for c in range(9, -1, -1):  # 비트 오른쪽에서 왼쪽으로 탐색
            if lst[r] & (1 << c):  # 현재 위치에 1이 있을 때만 진행
                for size in range(5, 0, -1):  # 큰 색종이부터 작은 색종이까지 확인
                    if r + size > 10 or c - size + 1 < 0:  # 범위를 벗어나면 건너뜀
                        continue
                    if papers[size] <= 0:  # 색종이를 모두 사용했으면 건너뜀
                        continue

                    # 현재 위치에 색종이 놓기 가능 여부 확인
                    mask = (1 << size) - 1 << (c - size + 1)  # size 크기 색종이 비트 마스크
                    temp_board = lst[:]

                    # 모든 행에 대해 색종이 크기만큼 확인 및 적용
                    can_place = all((temp_board[r + i] & mask) == mask for i in range(size))
                    if can_place:
                        # 색종이 놓기
                        for i in range(size):
                            temp_board[r + i] ^= mask
                        papers[size] -= 1

                        # 재귀 호출
                        checkcheck(temp_board, count + 1, r)

                        # 백트래킹: 놓은 색종이 제거
                        for i in range(size):
                            temp_board[r + i] ^= mask
                        papers[size] += 1
                return


# 초기 호출
checkcheck(board, 0, 0)

# 결과 출력
print(-1 if paper_count == 26 else paper_count)
