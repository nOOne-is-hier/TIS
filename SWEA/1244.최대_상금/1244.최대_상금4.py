def find_consecutive_indices(num):
    prev_char = None
    for idx in range(len(num)):
        if num[idx] == prev_char:
            return True
        prev_char = num[idx]


def swap_panels(case, swap_left=0, count_swap=0, best_case=None, direction="left", is_consecutive=False):
    # 결과를 저장할 변수
    if not best_case:
        best_case = [int(''.join(case))]

    # 횟수만큼 수행 완료
    if count_swap == swap_left:
        best_case[0] = max(best_case[0], int(''.join(case)))
        return best_case[0]

    # 최선의 경우에 도달했는가?, 종료
    current = int(''.join(case))
    if current == max_case:
        if is_consecutive:
            # 연속된 숫자가 있으면 바로 종료
            best_case[0] = current
            return best_case[0]
        else:
            # 남은 스왑 횟수에 따라 마지막 두 자리를 교환
            if (swap_left - count_swap) % 2 == 0:
                best_case[0] = current
            else:
                case = list(case)
                case[-1], case[-2] = case[-2], case[-1]
                best_case[0] = int(''.join(case))
            return best_case[0]

    # case를 리스트로 분해
    case = list(case)

    # 최선의 수행 (왼쪽 -> 오른쪽)
    if direction == "left":
        max_orders = sorted([(int(case[idx]), idx) for idx in range(len(case))], key=lambda x: (x[0], x[1]),
                            reverse=True)
        min_orders = sorted([(idx, int(case[idx])) for idx in range(len(case))], key=lambda x: (x[0], x[1]))

        for pointer in range(len(case) - 1):
            if max_orders[pointer][1] != pointer and (
                    max_orders[pointer][1] == len(case) - 1 or case[max_orders[pointer][1]] != case[
                max_orders[pointer][1] + 1]):
                for cursor in range(len(case)):
                    if max_orders[pointer][0] > min_orders[cursor][1] and max_orders[pointer][1] > min_orders[cursor][
                        0]:
                        case[max_orders[pointer][1]], case[min_orders[cursor][0]] = case[min_orders[cursor][0]], case[
                            max_orders[pointer][1]]
                        return swap_panels(''.join(map(str, case)), swap_left, count_swap + 1, best_case, "left",
                                           is_consecutive)

    # 반대 방향 수행 (오른쪽 -> 왼쪽)
    elif direction == "right":
        max_orders = sorted([(int(case[idx]), idx) for idx in range(len(case))], key=lambda x: (x[0], -x[1]),
                            reverse=True)
        for i in range(len(case) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if case[j] < case[i]:
                    case[j], case[i] = case[i], case[j]
                    return swap_panels(''.join(map(str, case)), swap_left, count_swap + 1, best_case, "right",
                                       is_consecutive)

    return best_case[0]


for tc in range(1, int(input()) + 1):
    # 입력
    first_case, exchange_num = input().split()
    max_case = int(''.join(sorted(first_case, reverse=True)))
    is_consecutive = find_consecutive_indices(str(max_case))

    # 왼쪽에서 오른쪽으로 탐색
    result_left = swap_panels(list(first_case), swap_left=int(exchange_num), direction="left",
                              is_consecutive=is_consecutive)

    # 오른쪽에서 왼쪽으로 탐색
    result_right = swap_panels(list(first_case), swap_left=int(exchange_num), direction="right",
                               is_consecutive=is_consecutive)

    # 두 결과 중 최댓값을 선택
    result = max(result_left, result_right)
    print(f'#{tc} {result}')