import sys
sys.stdin = open('input.txt')

words = list(map(str, input().split()))
print(len(words))