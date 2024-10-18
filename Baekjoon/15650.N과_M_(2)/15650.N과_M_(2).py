import sys
sys.stdin = open('input.txt')

N, M = list(map(int, input().split()))

numbers = list(range(1, N + 1))
arrays = []

def combination(case=[], is_in_list=[0]*len(numbers)):
    copy_case = case[:]
    copy_list = is_in_list[:]

    if len(copy_case) == M:
        arrays.append(sorted(copy_case))
        return

    for idx in range(len(numbers)):
        if copy_list[idx]:
            continue

        copy_list[idx] = 1
        copy_case.append(numbers[idx])
        combination(copy_case, copy_list)
        copy_case.pop()
        # copy_list[idx] = 0

combination()

for array in arrays:
    print(*array)