import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

length = int(input())
heights = list(map(int, input().split()))

uphills = []
current_uphill = 0

for idx in range(1, length):
    if heights[idx] > heights[idx - 1]:
        current_uphill += heights[idx] - heights[idx - 1]
    else:
        if current_uphill > 0:
            uphills.append(current_uphill)
        current_uphill = 0

# 마지막 오르막길 처리
if current_uphill > 0:
    uphills.append(current_uphill)

if uphills:
    print(max(uphills))
else:
    print(0)
