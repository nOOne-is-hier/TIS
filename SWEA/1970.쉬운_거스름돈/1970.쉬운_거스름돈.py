import sys
from collections import OrderedDict
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    change = int(input())
    # 무야호
    currency = OrderedDict()
    currency.setdefault(50000, 0)
    currency.setdefault(10000, 0)
    currency.setdefault(5000, 0)
    currency.setdefault(1000, 0)
    currency.setdefault(500, 0)
    currency.setdefault(100, 0)
    currency.setdefault(50, 0)
    currency.setdefault(10, 0)

    for bill in currency:
        currency[bill] += change // bill
        change %= bill

    print(f'#{tc}\n' + ' '.join(map(str, currency.values())))
