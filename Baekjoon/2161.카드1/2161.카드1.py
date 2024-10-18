import sys
sys.stdin = open('input.txt')

from collections import deque

deck = deque(range(int(input()), 0, -1))

while deck:
    print(deck.pop(), end=' ')
    if deck:
        deck.appendleft(deck.pop())