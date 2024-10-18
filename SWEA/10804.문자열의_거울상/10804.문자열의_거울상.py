import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    word = input()

    # 방법1. reversed()
    '''print(f'#{tc}', end=' ')
    for letter in reversed(word):
        if letter == 'b':
            print('d', end='')
        elif letter == 'd':
            print('b', end='')
        elif letter == 'q':
            print('p', end='')
        elif letter == 'p':
            print('q', end='')
    print()
    print(reversed_word)'''

    # 방법2. 역 indexing
    '''reversed_word = [0] * len(word)
    for idx in range(len(word)-1, -1, -1):
        reversed_word[idx] = [word[len(word)-idx-1]]

    print(f'#{tc}', end=' ')
    for letter in reversed_word:
        if letter == ['b']:
            print('d', end='')
        elif letter == ['d']:
            print('b', end='')
        elif letter == ['q']:
            print('p', end='')
        elif letter == ['p']:
            print('q', end='')
    print()'''

    # 방법3. enumerate 사용
    '''reversed_word = [''] * len(word)

    for idx, letter in enumerate(word):
        if letter == 'b':
            reversed_word[len(word)-1-idx] = 'd'
        elif letter == 'd':
            reversed_word[len(word)-1-idx] = 'b'
        elif letter == 'p':
            reversed_word[len(word)-1-idx] = 'q'
        elif letter == 'q':
            reversed_word[len(word)-1-idx] = 'p'

    print(f'#{tc}', ''.join(reversed_word))'''

    '''# 방법4. replace 활용
    reversed_word = ''.join(reversed(word))
    mirrored_reversed_word = (
        reversed_word.replace('b', '1')
        .replace('d', 'b')
        .replace('1', 'd')
        .replace('q', '2')
        .replace('p', 'q')
        .replace('2', 'p')
    )

    print(f'#{tc}', mirrored_reversed_word)'''

    # 방법5. 딕셔너리를 활용
    '''char_dict = {'b': 'd', 'd': 'b', 'q': 'p', 'p': 'q'}
    reversed_word = ''.join([char_dict[letter] for letter in reversed(word)])
    print(f'#{tc}', reversed_word)'''

    # 방법6. append 활용
    '''reversed_word = []

    for letter in reversed(word):
        if letter == 'b':
            reversed_word.append('d')
        elif letter == 'd':
            reversed_word.append('b')
        elif letter == 'q':
            reversed_word.append('p')
        elif letter == 'p':
            reversed_word.append('q')

    print(f'#{tc}', ''.join(reversed_word))'''

    # 방법7. str. 클래스 함수 사용하기
    '''transtab = str.maketrans({'b': 'd', 'd': 'b', 'q': 'p', 'p': 'q'})

    reversed_word = ''.join(reversed(word)).translate(transtab)

    print(f'#{tc}', reversed_word)'''

    # 방법8. 극한의 최적화를 해보자
    trantab = str.maketrans('bdpq', 'dbqp')
    result = []
    for char in reversed(word):
        result.append(char.translate(trantab))
    print(f'#{tc} {"".join(result)}')
