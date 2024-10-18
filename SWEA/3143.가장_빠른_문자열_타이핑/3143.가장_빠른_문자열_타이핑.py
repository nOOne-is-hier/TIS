import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()

    number = 0
    idx = 0
    # 문자열을 찾아내면 다음 위치로 넘어가야 함. 중복이 존재할 수 있음
    while idx <= len(A) - len(B):
        if A[idx:idx+len(B)] == B:
            number += 1
            idx += len(B)  # B를 찾은 위치 다음으로 이동
        else:
            idx += 1  # 한 글자씩 이동

    # 올바른 결과 계산
    result = len(A) - (len(B) - 1) * number
    print(f'#{tc} {result}')
