import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

length = int(input())
heights = list(map(int, input().split())) + [0]

start = heights[0]
end = heights[-1]
idx = -1
uphills = []

for height in heights:
    idx += 1
    if 0 <= idx - 1 < len(heights):
        if height <= heights[idx-1]:
            start = height
        elif height > heights[idx+1]:
            end = height
            uphills += [end - start]
            start = end = 0

if uphills:
    print(max(uphills))
else:
    print(0)