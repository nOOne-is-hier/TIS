import sys
sys.stdin = open('input.txt')

N, M = list(map(int, input().split()))

numbers = list(range(1, N + 1))
arrays = []

def permutaion(case=[], is_in_list=[0]*len(numbers)):
    copy_list = is_in_list[:]
    copy_case = case[:]

    if len(copy_case) == M:
        arrays.append(copy_case)
        return

    for idx in range(len(numbers)):

        if copy_list[idx]:
            continue

        else:
            copy_list[idx] = 1
            copy_case.append(numbers[idx])
            permutaion(copy_case, copy_list)
            copy_case.pop()
            copy_list[idx] = 0

permutaion()

for array in arrays:
    print(*array)
