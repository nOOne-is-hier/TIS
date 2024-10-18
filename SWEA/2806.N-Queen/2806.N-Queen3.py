import sys
sys.stdin = open('input.txt')


def n_queen(top=0, array=None, cases=None):
    if not array:
        array = [0] * (N + 1)

    if not cases:
        cases = [0]

    if promising(top, array):
        if top == N:
            cases[0] += 1

        else:
            for new in range(1, N + 1):
                array[top+1] = new
                n_queen(top+1, array, cases)

    return cases[0]

def promising(new, array):
    idx = 1
    while idx < new:
        if array[new] == array[idx] or abs(array[new] - array[idx]) == new - idx:
            return False
        idx += 1
    return True

for tc in range(1, int(input()) + 1):
    N = int(input())

    result = n_queen()

    print(f'#{tc} {result}')
