import sys
sys.stdin = open('input.txt')

T = int(input())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


for tc in range(1, T + 1):
    N = int(input())
    total_try = 0
    max_try = int(N/10)
    min_try = N//20 + int(N%20/10)

    for length in range(min_try, max_try+1):
        array = [1] * length
        for idx in range(max_try-length):
            array[idx] = 2

        count_try = int(factorial(len(array))/factorial(length-(max_try-length))/factorial((max_try-length)))
        count_try *= (2**(max_try-length))
        total_try += count_try
    print(f'#{tc} {total_try}')