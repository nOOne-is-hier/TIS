import sys
sys.stdin = open('input.txt')
from decimal import Decimal, ROUND_HALF_UP

for tc in range(1, int(input()) + 1):
    N = int(input())

    deck = input().split()

    perfect_shuffle = []
    split_point = int(Decimal(N/2).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

    front_deck = deck[:split_point]
    rear_deck = deck[split_point:]

    while front_deck or rear_deck:
        if front_deck:
            perfect_shuffle.append(front_deck.pop(0))
        if rear_deck:
            perfect_shuffle.append(rear_deck.pop(0))

    print(f'#{tc} {" ".join(perfect_shuffle)}')