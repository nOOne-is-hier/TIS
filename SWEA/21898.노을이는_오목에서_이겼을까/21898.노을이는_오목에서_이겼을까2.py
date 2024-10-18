import sys
sys.stdin = open('input.txt')


def who_win(r, c):
    
    # 4방향 탐색
    for dir in range(4):
        discriminator = [goban[r][c]]
        coordinates = [(r, c)]
        wrong_dir = False
        
        # 육목 검증
        for is_sixth in range(2):
            mmr = r + (dr[dir]*mr[is_sixth])
            mmc = c + (dc[dir]*mc[is_sixth])
            if 0 <= mmr < 19 and 0 <= mmc < 19:
                if goban[mmr][mmc] == goban[r][c]:
                    wrong_dir = True
                    break
        if wrong_dir:
            continue
        
        # 오목 검증
        for dis in range(1, 5):
            nr = r + (dr[dir]*dis)
            nc = c + (dc[dir]*dis)
            if 0 <= nr < 19 and 0 <= nc < 19:
                if goban[nr][nc] != discriminator[0]:
                    break

                discriminator.append(goban[nr][nc])
                coordinates.append((nr, nc))

        if len(discriminator) == 5:
            # 게임 종료
            global is_playing
            is_playing = False
            # 승자 선택
            winner = 'Noheul WIN!' if goban[r][c] == 1 else 'Noheul LOSE T.T'
            # 승착 좌표
            y, x = min(coordinates, key=lambda coordinate: (coordinate[1], coordinate[0]))
            print(f'{winner} {y+1, x+1}')


T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    goban = [list(map(int, input().split())) for _ in range(19)]
    is_playing = True

    # 8방위의 절반만 탐색
    dr = [0, 1, 1, 1]
    dc = [1, 1, 0, -1]
    mr = [-1, 5]
    mc = [-1, 5]

    # 바둑판을 순회하며 1또는 2를 찾으면 시작
    for r in range(19):
        for c in range(19):
            if any(goban[r][c] == x for x in (1, 2)) and is_playing:
                who_win(r, c)

    if is_playing:
        print('PLAYING')