import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

# 초기화
S, P = map(int, input().split())
raw_text = input().strip()
A, C, G, T = map(int, input().split())

required_count = {'A': A, 'C': C, 'G': G, 'T': T}
count_letters = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
promise_case = 0

# 유효성 검증 함수 (대소 비교 사용)
def is_valid():
    for key in 'ACGT':
        if count_letters[key] < required_count[key]:
            return False
    return True

# 슬라이딩 윈도우 초기화
for letter in raw_text[:P]:
    count_letters[letter] += 1

# 초기 윈도우 유효성 검사
if is_valid():
    promise_case += 1

# 슬라이딩 윈도우 실행
for idx in range(P, S):
    # 왼쪽 문자 제거
    count_letters[raw_text[idx - P]] -= 1
    # 오른쪽 문자 추가
    count_letters[raw_text[idx]] += 1
    # 현재 윈도우 유효성 검사
    if is_valid():
        promise_case += 1

print(promise_case)
