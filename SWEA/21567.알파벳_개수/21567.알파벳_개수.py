import sys
sys.stdin = open('input.txt')

T = int(input())

'''for tc in range(1, T + 1):
    count_alphabet = {chr(ord('a') + i): 0 for i in range(26)}
    for letter in input():
        count_alphabet[letter] += 1
        
    print(f'#{tc}', *count_alphabet.values())'''

for tc in range(1, T + 1):
    count_alphabet = [0] * 26
    for letter in input():
        count_alphabet[ord(letter)-97] += 1

    print(f'#{tc}', *count_alphabet)