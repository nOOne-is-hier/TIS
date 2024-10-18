import sys
sys.stdin = open('input.txt')

dwarfs = list(map(int, sys.stdin.read().split()))

fakes_height = sum(dwarfs) - 100

for i in range(len(dwarfs)):
    for j in range(i+1, len(dwarfs)):
        a = dwarfs[i]
        b = dwarfs[j]
        if a + b == fakes_height:
            dwarfs.remove(a)
            dwarfs.remove(b)
            break

    else:
        continue

    break

for i in range(len(dwarfs)):
    min_idx = i

    for j in range(i+1, len(dwarfs)):
        if dwarfs[j] < dwarfs[min_idx]:
            min_idx = j

    dwarfs[i], dwarfs[min_idx] = dwarfs[min_idx], dwarfs[i]

'''for i in range(len(dwarfs)):
    for j in range(i+1, len(dwarfs)):
        if dwarfs[i] > dwarfs[j]:
            dwarfs[i], dwarfs[j] = dwarfs[j], dwarfs[i]'''

for dwarf in dwarfs:
    print(dwarf)