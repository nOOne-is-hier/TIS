import sys
sys.stdin = open('input.txt')

dwarfs = list(map(int, sys.stdin.read().split()))


def find_real_dwarf(population=0, isinvolved=[0]*len(dwarfs), case=[]):
    isinvolved_copy = isinvolved[:]
    case_copy = case[:]

    # 7명, 합 100, 이면 반환
    if population == 7 and sum(case_copy) == 100:
        case_copy.sort()
        print('\n'.join(map(str, case_copy)))
        return True

    elif population > 7 or sum(case_copy) > 100:
        return False

    for num in range(len(dwarfs)):
        if isinvolved_copy[num]:
            continue

        isinvolved_copy[num] = 1
        case_copy.append(dwarfs[num])
        if find_real_dwarf(population+1, isinvolved_copy, case_copy):
            return True
        case_copy.pop()
        isinvolved_copy[num] = 0


find_real_dwarf()