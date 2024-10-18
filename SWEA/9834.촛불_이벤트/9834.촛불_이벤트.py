import math

T = int(input())
inputs = [int(input()) for _ in range(T)]
results = []

for tc in range(1, T + 1):
    N = inputs[tc - 1]
    discriminant = 8 * N + 1
    value = math.isqrt(discriminant)

    if value * value == discriminant:
        results.append(f"#{tc} {((value - 1) // 2)}")
    else:
        results.append(f"#{tc} -1")

print("\n".join(results))
