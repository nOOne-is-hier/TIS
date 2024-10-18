import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N, word = map(str, input().split())
    for letter in word:
        print(letter*int(N), end='')
    print()