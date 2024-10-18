import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())

    tree_array = [0] * (N + 1)

    idx = 0
    for num in map(int, input().split()):
        idx += 1
        tree_array[idx] = num
        temp_idx = idx

        while temp_idx // 2:
            if tree_array[temp_idx] < tree_array[temp_idx // 2]:
                tree_array[temp_idx], tree_array[temp_idx // 2] = \
                tree_array[temp_idx // 2], tree_array[temp_idx]

            temp_idx //= 2
    result = 0
    last = len(tree_array) - 1
    while last // 2:
        last //= 2
        result += tree_array[last]

    print(f'#{tc} {result}')