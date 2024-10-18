import sys

sys.stdin = open('input.txt')

T = int(input())

# 리스트를 분할 할 수 없을 때까지 분할하고 병합정렬하는 재귀함수
def devide_array(lst):
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    llst = lst[:middle]
    rlst = lst[middle:]

    return merge_sort(devide_array(llst), devide_array(rlst))

# 두 개의 리스트의 에서 요소를 각각 뽑아 비교해 새로운 리스트에 반환하는 함수
def merge_sort(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append((right[j]))
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

for tc in range(1, T + 1):
    length = int(input())
    array = list(map(int, input().split()))

    result = devide_array(array)
    print(f'#{tc}', *result)
