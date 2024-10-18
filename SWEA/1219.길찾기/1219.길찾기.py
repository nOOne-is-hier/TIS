import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case, num_ordered = map(int, input().split())
    coordinates = list(map(int, input().split()))

    array1 = [0] * 100
    array2 = [0] * 100

    for i in range(0, len(coordinates), 2):
        if not array1[coordinates[i]]:
            array1[coordinates[i]] = coordinates[i+1]
        array2[coordinates[i]] = coordinates[i+1]

    lasts_stack = [0]
    last = array1[0]
    arrived = True
    while last != 99:
        if 0 < array1[last]:
            lasts_stack.append(last)
            last = array1[last]
            array1[lasts_stack[-1]] = 0
        elif array2[last] != 0:
            lasts_stack.append(last)
            last = array2[last]
            array2[lasts_stack[-1]] = 0
        else:
            if not lasts_stack[-1]:
                arrived = False
                break
            last = array2[lasts_stack.pop()]

    print(f'#{test_case} {int(arrived)}')