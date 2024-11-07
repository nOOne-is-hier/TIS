import sys
input = sys.stdin.read

N, *numbers = map(int, input().split())
p, m, r = [], [], 0

for n in numbers:
    if n > 1:
        p.append(n)
    elif n <= 0:
        m.append(n)
    else:
        r += 1  # n == 1인 경우 결과에 바로 추가

# 내림차순 정렬된 양수와 오름차순 정렬된 음수
p.sort(reverse=True)
m.sort()

# 양수 처리
for i in range(0, len(p) - 1, 2):
    r += p[i] * p[i + 1]
if len(p) % 2 == 1:
    r += p[-1]

# 음수 처리
for i in range(0, len(m) - 1, 2):
    r += m[i] * m[i + 1]
if len(m) % 2 == 1:
    r += m[-1]

print(r)
