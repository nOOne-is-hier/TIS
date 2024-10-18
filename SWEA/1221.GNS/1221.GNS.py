import sys
sys.stdin = open('input.txt')
<<<<<<< HEAD
sys.stdout = open('output.txt', 'w')
=======
>>>>>>> 9fe6f12b02157a48ff8ada985b87ed1f42bb79ae

T = int(input())

for tc in range(1, T + 1):
    _ = input()
    words = input().split()
    count_word = {}

    for word in words:
        count_word.setdefault(word, 0)
        count_word[word] += 1
<<<<<<< HEAD
    print(f'#{tc}')
    print('ZRO ' * count_word['ZRO'], end='')
    print('ONE ' * count_word['ONE'], end='')
    print('TWO ' * count_word['TWO'], end='')
    print('THR ' * count_word['THR'], end='')
    print('FOR ' * count_word['FOR'], end='')
    print('FIV ' * count_word['FIV'], end='')
    print('SIX ' * count_word['SIX'], end='')
    print('SVN ' * count_word['SVN'], end='')
    print('EGT ' * count_word['EGT'], end='')
    print('NIN ' * count_word['NIN'])
=======

    print('ZRO' * count_word['ZRO'])
>>>>>>> 9fe6f12b02157a48ff8ada985b87ed1f42bb79ae
