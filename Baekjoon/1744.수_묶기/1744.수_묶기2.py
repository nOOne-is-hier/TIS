import sys

sys.stdin = open('input.txt')

N = int(input())

pluses = []
minuses = []
result = 0
for _ in range(N):
    num = int(input())
    if num > 1:
        pluses.append(num)
    elif num <= 0:
        minuses.append(num)
    else:
        result += 1

pluses.sort(reverse=True)
minuses.sort()
for cnt in range(0, len(minuses), 2):
    if cnt + 1 < len(minuses):
        result += minuses[cnt] * minuses[cnt + 1]
    else:
        result += minuses[cnt]
for cnt in range(0, len(pluses), 2):
    if cnt + 1 < len(pluses):
        result += pluses[cnt] * pluses[cnt + 1]
    else:
        result += pluses[cnt]
print(result)