import sys
from collections import defaultdict

sys.stdin = open('input.txt')

input = sys.stdin.readline

def collect_letter(letter):
    global split_way
    
    if letter == 'q':
        DAT['q'] += 1
        split_way = max(split_way, sum(DAT.values()))
    
    elif letter == 'u':
        if DAT['q']:
            DAT['q'] -= 1
            DAT['u'] += 1
        else:
            print(-1)
            exit()
            
    elif letter == 'a':
        if DAT['u']:
            DAT['u'] -= 1
            DAT['a'] += 1
        else:
            print(-1)
            exit()
            
    elif letter == 'c':
        if DAT['a']:
            DAT['a'] -= 1
            DAT['c'] += 1
        else:
            print(-1)
            exit()
            
    elif letter == 'k':
        if DAT['c']:
            DAT['c'] -= 1
        else:
            print(-1)
            exit()
            

raw_text = input().strip()

DAT = defaultdict(int)
split_way = 0

for letter in raw_text:
    if letter in 'quack':
        collect_letter(letter)

if sum(DAT.values()):
    print(-1)
    exit()
else:
    print(split_way)