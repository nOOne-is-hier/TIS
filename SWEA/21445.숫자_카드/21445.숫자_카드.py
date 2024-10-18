import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    card_order = input()

    number_of_cards_per_num = {}
    for num in range(10):
        number_of_cards_per_num[str(num)] = 0

    for num in card_order:
        number_of_cards_per_num[num] += 1

    card, counts = max(number_of_cards_per_num.items(), key=lambda item: (item[1], item[0]))

    print(f'#{tc}', int(card), counts)