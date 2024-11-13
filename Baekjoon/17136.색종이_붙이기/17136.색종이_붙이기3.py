import sys
from functools import lru_cache
sys.stdin = open('input.txt')
input = sys.stdin.readline

def paste_papers():
    board = tuple(tuple(map(int, input().split())) for _ in range(10))
    papers = (5, 5, 5, 5, 5)

    @lru_cache(None)
    def dfs(r, c, board, papers, count):
        # 모든 행을 검사한 경우 종료
        if r == 10:
            return count

        # 다음 행으로 이동
        if c == 10:
            return dfs(r + 1, 0, board, papers, count)

        # 이미 덮인 부분이면 다음 칸으로 이동
        if board[r][c] == 0:
            return dfs(r, c + 1, board, papers, count)

        # 가능한 최소 종이 수를 찾기 위해 초기값 설정
        min_papers = float('inf')
        can_cover = False  # 이 위치에서 종이를 놓을 수 있는지 확인

        # 가능한 종이 크기를 시도하여 최소 종이 수 찾기
        for size in range(5, 0, -1):
            if papers[size - 1] > 0 and can_place(r, c, size, board):
                can_cover = True
                # 종이를 놓은 새로운 상태 만들기
                new_board = place_paper(r, c, size, board)
                new_papers = list(papers)
                new_papers[size - 1] -= 1
                # 재귀 호출로 탐색 진행
                min_papers = min(min_papers, dfs(r, c + size, new_board, tuple(new_papers), count + 1))

        # 종이를 놓을 수 없는 경우 `-1` 반환을 위해 확인
        if not can_cover:
            return float('inf')

        return min_papers

    def can_place(r, c, size, board):
        """ Checks if a paper of given size can be placed at (r, c). """
        if r + size > 10 or c + size > 10:
            return False
        return all(board[i][j] == 1 for i in range(r, r + size) for j in range(c, c + size))

    def place_paper(r, c, size, board):
        """ Places a paper of given size at (r, c) and returns a new board state. """
        board = [list(row) for row in board]
        for i in range(r, r + size):
            for j in range(c, c + size):
                board[i][j] = 0
        return tuple(map(tuple, board))  # Make board hashable for caching

    result = dfs(0, 0, board, papers, 0)
    return -1 if result == float('inf') else result

print(paste_papers())
