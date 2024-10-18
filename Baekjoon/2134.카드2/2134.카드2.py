import sys
sys.stdin = open('input.txt')

from collections import deque

deck = deque(range(int(input()), 0, -1))

while deck:
    last = deck.pop()

    if deck:
        deck.appendleft(deck.pop())

print(last)