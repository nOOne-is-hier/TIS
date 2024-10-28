import sys

sys.stdin = open('input.txt')

A, B = map(int, input().split())
base = A

divisor = 10 ** 9 + 7
A **= B
result = (A - 1) // (base - 1)
print(result)