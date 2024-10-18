import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())

    tree_array = [0] * N ** 2
    index_list = {}
    idx = 0
    for _ in range(N):
        for num in map(int, input().split()):
            tree_array[idx] = num
            index_list[num] = idx
            idx += 1

    # 델타 배열
    d_idx = [1, N, -1, -N]

    for idx in range(1, N ** 2 + 1):
        if type(index_list[idx]) != str :
            for dir in range(4):
                n_idx = index_list[idx] + d_idx[dir]
                if index_list[idx] // N == n_idx // N\
                        and (index_list[tree_array[n_idx]] or index_list[tree_array[n_idx]] == 0):
                    index_list[tree_array[n_idx]] = 'EXPLODED'

                elif ((dir == 1 or dir == 3) and 0 <= n_idx < N ** 2)\
                        and (index_list[tree_array[n_idx]] or index_list[tree_array[n_idx]] == 0):
                    index_list[tree_array[n_idx]] = 'EXPLODED'

            last_explode = idx
            index_list[idx] = 'EXPLODED'

        else:
            continue

    print(f'#{tc} {last_explode}초')