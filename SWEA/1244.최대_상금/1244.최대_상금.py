import sys
sys.stdin = open('input.txt')


def find_consecutive_indices(num):
    prev_char = None
    for idx in range(len(num)):
        if num[idx] == prev_char:
            return idx - 1, idx
        prev_char = num[idx]


def swap_panels(case, is_consecutive, count_swap=0, is_max=False):
    # 횟수만큼 수행 완료
    if str(count_swap) == exchange_num:
        return case
    # 최선을 만들기 위한 스왑이 아닌, 버티기 위한 스왑
    if case == max_case:
        is_max = True
    # case를 대소 비교가 가능한 list로 분해
    case = list(map(int, case))
    # 최선의 수행
    if not is_max:
        # 최대 힙
        max_orders = sorted([(int(case[idx]), idx) for idx in range(len(case))], key=lambda x: (x[0], x[1]), reverse=True)
        # 최소 힙
        min_orders = sorted([(idx, int(case[idx])) for idx in range(len(case))], key=lambda x: (x[0], x[1]))
        # 큰 값부터 검사 시작
        for pointer in range(len(case)-1):
            # 위치가 맞지 않고, 같은 수가 연속한 것이 아니라면
            if max_orders[pointer][1] != pointer and (max_orders[pointer][1] == len(case)-1 or case[max_orders[pointer][1]] != case[max_orders[pointer][1]+1]):
                # 작은 값부터 치환할 자리 탐색
                for cursor in range(len(case)):
                    # 값이 더 크고, 인덱스가 더 크면(뒤면) SWAP!
                    if max_orders[pointer][0] > min_orders[cursor][1] and max_orders[pointer][1] > min_orders[cursor][0]:
                        case[max_orders[pointer][1]], case[min_orders[cursor][0]] = case[min_orders[cursor][0]], case[max_orders[pointer][1]]
                        return swap_panels(''.join(map(str, case)), is_consecutive, count_swap+1, is_max)
    # 버티는 수행
    if is_max:
        # 연속된 수가 있다면 럭키비키!!
        if is_consecutive:
            left, right = is_consecutive
            case[left], case[right] = case[right], case[left]
            return swap_panels(''.join(map(str, case)), is_consecutive, count_swap + 1, is_max)
        # 없다면 버티자
        else:
            case[-2], case[-1] = case[-1], case[-2]
            return swap_panels(''.join(map(str, case)), is_consecutive, count_swap + 1, is_max)


for tc in range(1, int(input()) + 1):
    # 입력
    first_case, exchange_num = input().split()
    # 최선의 결과
    max_case = ''.join(map(str, sorted(list(map(int, first_case)), reverse=True)))
    # 최선의 결과에 연속된 숫자가 있는가?
    is_consecutive = find_consecutive_indices(max_case)
    # 출력
    print('#{} {}'.format(tc, swap_panels(first_case, is_consecutive)))