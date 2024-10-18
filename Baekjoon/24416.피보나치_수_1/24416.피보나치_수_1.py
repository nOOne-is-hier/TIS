import sys
sys.stdin = open('input.txt')
N = int(input())
result = [1, 1]
res = 0
num = 0
for cnt in range(2, N):
    res = result[-2] + result[-1]
    result += [res]
    num += 1

print(res, num)