import sys
sys.stdin = open('input.txt')

N, S = list(map(int, input().split()))
numbers = list(map(int, input().split()))

issum_S = 0


def find_subsets(num=0, subset=[]):
    global issum_S
    for i in range(num, N):
        subset.append(numbers[i])
        if sum(subset) == S:
            issum_S += 1
        find_subsets(i+1, subset)
        subset.pop()

find_subsets()
print(issum_S)
