import sys
sys.stdin = open('input.txt')

A, B = list(map(str, input().split()))

A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)