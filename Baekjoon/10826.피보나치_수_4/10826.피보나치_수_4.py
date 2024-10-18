import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
if N == 0:
    print(N)
elif N == 1:
    print(N)
else:
    array = [0] * (N+1)
    array[1] = 1
    for num in range(2, N+1):
        array[num] = array[num-1] + array[num-2]
    print(array[-1])