import sys
sys.stdin = open('input.txt')


def find_consecutive_indices(num):
    prev_char = None
    for idx in range(len(num)):
        if num[idx] == prev_char:
            return idx - 1, idx
        prev_char = num[idx]


def swap_panels(case, is_consecutive, swap_left, idx=0, best_case=None):
    # 결과를 저장할 변수
    if not best_case:
        best_case = [int(''.join(case))]
    # 기저 조건, 모든 수행 완료
    if not swap_left:
        best_case[0] = max(best_case[0], int(''.join(case)))
        return
    # 최선의 경우에 도달 했는가?, 종료
    current = int(''.join(case))
    if current == max_case:
        if is_consecutive:
            best_case[0] = current
            return best_case[0]
        # 연속된 숫자가 없다면
        else:
            if swap_left % 2 == 0:
                best_case[0] = current
                return best_case[0]
            else:
                # 마지막 두 자리를 교환하여 최적화를 수행
                case[-1], case[-2] = case[-2], case[-1]
                best_case[0] = int(''.join(case))
                return best_case[0]

    # 가장 큰 수를 target
    max_digit = max(case[idx:])
    # 나 자신을 가리킨다면 pass
    if case[idx] == max_digit:
        swap_panels(case, is_consecutive, swap_left, idx + 1, best_case)

    else:
        for cursor in range(idx + 1, len(case)):
            if case[cursor] == max_digit:
                case[idx], case[cursor] = case[cursor], case[idx]
                swap_panels(case, is_consecutive, swap_left - 1, idx + 1, best_case)
                case[idx], case[cursor] = case[cursor], case[idx]   # 백트래킹
    return best_case[0]


for tc in range(1, int(input()) + 1):
    # 입력
    first_case, exchange_num = input().split()
    # 최선의 결과
    max_case = int(''.join(map(str, sorted(list(map(int, first_case)), reverse=True))))
    # 최선의 결과에 연속된 숫자가 있는가?
    is_consecutive = find_consecutive_indices(str(max_case))
    # 출력
    print('#{} {}'.format(tc, swap_panels(list(first_case), is_consecutive, int(exchange_num))))