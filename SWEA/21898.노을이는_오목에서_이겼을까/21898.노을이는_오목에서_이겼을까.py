import sys
sys.stdin = open('input.txt')


def who_win(r, c):

    for dir in range(8):
        discriminator = [goban[r][c]]
        coordinates = [(r, c)]
        for dis in range(1, 6):
            nr = r + (dr[dir]*dis)
            nc = c + (dc[dir]*dis)
            mr = r + (dr[dir]*-1)
            mc = c + (dc[dir]*-1)
            if 0 <= mr < 19 and 0 <= mc < 19:
                if goban[mr][mc] == goban[r][c]:
                    break
            if 0 <= nr < 19 and 0 <= nc < 19:
                if (dis < 5 and goban[nr][nc] != discriminator[0]) or (dis == 5 and goban[nr][nc] == discriminator[0]):
                    break
                else:
                    discriminator.append(goban[nr][nc])
                    coordinates.append((nr, nc))

        if len(discriminator) == 6 and len(set(discriminator)) == 2:
            # 게임 종료
            global is_playing
            is_playing = False
            # 좌표 정리
            coordinates.pop()
            # 승자 선택
            winner = 'Noheul WIN!' if goban[r][c] == 1 else 'Noheul LOSE T.T'
            # 승착 좌표
            y, x = min(coordinates, key=lambda coordinate: (coordinate[1], coordinate[0]))
            print(f'{winner} {y+1, x+1}')
            return


T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    goban = [list(map(int, input().split())) for _ in range(19)]
    is_playing = True

    # 8방위 델타를 사용하자
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    # 바둑판을 순회하며 1또는 2를 찾으면 시작
    for r in range(19):
        for c in range(19):
            if any(goban[r][c] == x for x in (1, 2)) and is_playing:
                who_win(r, c)

    if is_playing:
        print('PLAYING')