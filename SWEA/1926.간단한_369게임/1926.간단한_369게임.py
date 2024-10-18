import sys
sys.stdin = open('input.txt')

# 369게임이 진행되는 구간
numbers = list(map(str, range(1, int(input())+1)))

# 결과를 저장할 mirror list 생성
result_array = [0] * len(numbers)

# 진행 구간을 순회하면서
for idx in range(len(numbers)):
    # 한 번이라도 박수를 치는지 검증
    if '3' in numbers[idx] or '6' in numbers[idx] or '9' in numbers[idx]:
        is_clap = True
    else:
        is_clap = False

    # 각 요소에 대해 평가 시작

    if not is_clap:
        result_array[idx] = numbers[idx]
    # 369규칙으로 치환한 결과를 저장할 변수
    else:
        result = ''
        for char in numbers[idx]:
            if is_clap and char in '369':
                result += '-'

        result_array[idx] = result

print(*result_array)