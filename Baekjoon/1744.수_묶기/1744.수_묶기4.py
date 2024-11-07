import os

# 표준 입력 파일 디스크립터를 통해 입력 받기
input_data = os.read(0, os.fstat(0).st_size).decode()
numbers = list(map(int, input_data.split()))

N = numbers[0]
p, m, r = [], [], 0  # 양수, 음수, 그리고 1의 개수

# 리스트 분할
for n in numbers[1:]:
    if n > 1:
        p.append(n)
    elif n <= 0:
        m.append(n)
    else:
        r += 1  # n == 1인 경우 바로 합산

# 내림차순으로 양수 리스트 정렬 및 오름차순으로 음수 리스트 정렬
p.sort(reverse=True)
m.sort()

# 양수 처리: 큰 값부터 두 개씩 묶어 곱
i = 0
while i + 1 < len(p):
    r += p[i] * p[i + 1]
    i += 2
if i < len(p):  # 남은 하나가 있으면 더하기
    r += p[i]

# 음수 처리: 작은 값부터 두 개씩 묶어 곱
j = 0
while j + 1 < len(m):
    r += m[j] * m[j + 1]
    j += 2
if j < len(m):  # 남은 하나가 있으면 더하기
    r += m[j]

# 표준 출력으로 결과를 직접 씁니다.
os.write(1, f"{r}\n".encode())
