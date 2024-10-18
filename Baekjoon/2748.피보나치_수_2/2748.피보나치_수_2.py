import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
# N = int(input())

array = [0] * (N+1)

for num in range(N+1):
    if num == 0:
        array[num] = 0
    elif num == 1:
        array[num] = 1
    else:
        array[num] = array[num-1] + array[num-2]

print(array[-1])