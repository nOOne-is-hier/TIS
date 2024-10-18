import sys
sys.stdin = open('input.txt')

N = int(input())
array = [0] * (N+1)
if N <= 1:
    print(N)
else:
    array[1] = 1
    for idx in range(2, N+1):
        array[idx] = (array[idx-2] + array[idx-1])%1000000007
    print(array[-1])
