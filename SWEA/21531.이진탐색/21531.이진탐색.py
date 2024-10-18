import sys

sys.stdin = open('input.txt')

T = int(input())

def binary_search(target, pages):
    left = pages[0]
    right = pages[-1]
    middle = int((left+right)/2)
    search_number = 1

    while target != middle:
        if target < middle:
            right = middle
        elif target > middle:
            left = middle

        search_number += 1
        middle = int((left+right)/2)

    return search_number

for tc in range(1, T + 1):
    P, Pa, Pb = list(map(int, input().split()))
    pages = list(range(1, P + 1))

    winner = 'A' if binary_search(Pa, pages) < binary_search(Pb, pages) else 'B' if binary_search(Pa, pages) > binary_search(Pb, pages) else 0
    print(f'#{tc}', winner)