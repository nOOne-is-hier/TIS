import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
results = []

for _ in range(T):
    N = int(input())
    nums = set()
    tmp = []

    for _ in range(N * 2):
        current_line = list(map(int, input().split()))
        discriminator = set(current_line)
        if not discriminator.intersection(nums):
            tmp.append(current_line)
            nums = nums.union(discriminator)
        else:
            encoded = current_line

    decoded = [0] * N
    # 각 행이 자신의 위치를 찾을 수 있도록 `which_idx`를 열 기준으로 찾음
    which_idx = next((c for c in range(N) if any(row[c] == encoded[c] for row in tmp)), None)

    # `decoded` 리스트를 `which_idx` 기준으로 채우기
    for row in tmp:
        idx = encoded.index(row[which_idx])
        decoded[idx] = row

    results.append(decoded)
# 출력 부분
print(*[" ".join(map(str, row)) for decoded in results for row in decoded], sep="\n")
