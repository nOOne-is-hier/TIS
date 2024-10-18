import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    word = input()
    ispalindrome = True
    for idx in range(len(word)//2):
        if word[idx] != word[len(word)-1-idx]:
            ispalindrome = False
            break

    print(f'#{tc} {int(ispalindrome)}')