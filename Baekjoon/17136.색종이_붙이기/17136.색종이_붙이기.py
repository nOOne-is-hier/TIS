import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_potentials():
    potentials = [[] for _ in range(5)]
    for r in range(10):
        for c in range(10):
            if paper[r][c] and (r, c) not in used:
                not_promise = False
                for dis in range(5):
                    right, bottom = c + dis, r + dis
                    if right < 10 and bottom < 10 and counts[dis + 1]:
                        is_valid = False
                        for row in range(r, bottom + 1):
                            if not paper[row][right] or (r, c) in used:
                                not_promise = True
                                break
                        else:
                            is_valid = True
                        for col in range(c, right + 1):
                            if not paper[bottom][col] or (r, c) in used:
                                not_promise = True
                                break
                        else:
                            if is_valid:
                                paper[r][c] = dis + 1
                    else:
                        not_promise = True
                    if not_promise:
                        break
                potentials[-paper[r][c]].append((r, c))
    return potentials


def place_pieces():
    possibilities = find_potentials()
    for size in range(-5, 0):
        if size != -1 and possibilities[size]:
            min_select = (126, )
            for r, c in possibilities[size]:
                total = sum(sum(row[c:c-size]) for row in paper[r:r-size])
                if min_select[0] > total:
                    min_select = (total, r, c)
            return -size, [(min_select[1], min_select[2])]
        elif size == -1:
            return -size, possibilities[size]


def cover_ones():
    ones = sum(sum(line) for line in paper)
    used_pieces = 0
    while len(used) < ones and 0 < any(counts.values()):
        size, ran = place_pieces()
        if size == 1:
            if len(ran) > 5:
                return -1
            used_pieces += len(ran)
            counts[1] -= len(ran)
            for r, c in ran:
                used.add((r, c))
                paper[r][c] = 0
        else:
            used_pieces += 1
            counts[size] -= 1
            r, c = ran[0]
            for row in range(r, r + size):
                for col in range(c, c + size):
                    used.add((row, col))
                    paper[row][col] = 0
    if len(used) < ones:
        return -1
    return used_pieces

paper = [list(map(int, input().split())) for _ in range(10)]
counts = {5: 5, 4: 5, 3: 5, 2: 5, 1: 5}
used = set()    # 방문 배열
print(cover_ones())