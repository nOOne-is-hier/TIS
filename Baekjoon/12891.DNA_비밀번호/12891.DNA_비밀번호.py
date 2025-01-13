import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def is_valid():
    global promise_case

    for k in 'ACGT':
        if required_count[k] > count_letters[k]:
            return

    promise_case += 1

S, P = map(int, input().split())

raw_text = input().strip()

A, C, G, T = map(int, input().split())

required_count = {'A': A, 'C': C, 'G': G, 'T': T}

count_letters = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

promise_case = 0

for letter in raw_text[:P]:
    count_letters[letter] += 1

is_valid()

if S != P:
    for idx in range(1, S - P + 1):
        count_letters[raw_text[idx - 1]] -= 1
        count_letters[raw_text[idx + P - 1]] += 1
        is_valid()

print(promise_case)