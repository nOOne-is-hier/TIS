import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
answers = [0] * T
for idx in range(T):
    l, r = map(int, input().split())
    diff = r - l
    if diff >= r / 2:
        answers[idx] = 'no'
    else:
        answers[idx] = 'yes'
print('\n'.join(answers))