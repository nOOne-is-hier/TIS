import sys
sys.stdin = open('input.txt')

price = int(input())
currencies = [500, 100, 50, 10, 5, 1]
result = 0
change = 1000 - price

for currency in currencies:
    result += change // currency
    change %= currency

print(result)