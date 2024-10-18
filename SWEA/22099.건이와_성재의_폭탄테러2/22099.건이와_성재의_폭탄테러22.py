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

    current = 0
    while index_list:
        current += 1
        if current in index_list:
            next_explode = index_list[current]
            index_list.pop(current)
            last_explode = current

            for dir in range(4):
                n_idx = next_explode + d_idx[dir]
                # 기존의 조건에서 추가적인 범위 검사를 추가
                if 0 <= n_idx < N ** 2 and tree_array[n_idx] in index_list \
                        and next_explode // N == n_idx // N \
                        and (index_list[tree_array[n_idx]] or index_list[tree_array[n_idx]] == 0):
                    index_list.pop(tree_array[n_idx])



                elif 0 <= n_idx < N ** 2 and tree_array[n_idx] in index_list \
                        and ((dir == 1 or dir == 3) and (index_list[tree_array[n_idx]] or index_list[tree_array[n_idx]] == 0)):

                    index_list.pop(tree_array[n_idx])

    print(f'#{tc} {last_explode}초')