import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def paste_papers():
    paper = [list(map(int, input().split())) for _ in range(10)]
    counts = {5: 5, 4: 5, 3: 5, 2: 5, 1: 5}

    min_papers = 25

    def can_place(r, c, size):
        """Checks if a paper of given size can be placed at (r, c)."""
        if r + size > 10 or c + size > 10:
            return False
        return all(paper[i][j] == 1 for i in range(r, r + size) for j in range(c, c + size))

    def place(r, c, size, value):
        """Places or removes a paper of given size at (r, c) by setting cells to value."""
        for i in range(r, r + size):
            for j in range(c, c + size):
                paper[i][j] = value

    def dfs(pieces):
        nonlocal min_papers

        # 최소 조각 수 업데이트
        if all(all(cell == 0 for cell in row) for row in paper):
            min_papers = min(min_papers, pieces)
            return

        # 더 이상 최소값을 갱신할 수 없으면 종료
        if pieces >= min_papers:
            return

        for r in range(10):
            for c in range(10):
                if paper[r][c] == 1:
                    for size in range(5, 0, -1):
                        if counts[size] > 0 and can_place(r, c, size):
                            place(r, c, size, 0)
                            counts[size] -= 1
                            dfs(pieces + 1)
                            place(r, c, size, 1)
                            counts[size] += 1
                    return  # 현재 위치에 대해 모든 경우를 탐색했으면 반환

    dfs(0)
    return -1 if min_papers == 25 else min_papers

print(paste_papers())
