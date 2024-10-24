def solve_modular_equation(A, B, C):
    mod = 10**9
    delta = (B * B - 4 * A * C) % mod
    if delta < 0: return -1
    sqrt_delta = pow(delta, (mod + 1) // 4, mod)  # Tonelli–Shanks
    x1 = (-B + sqrt_delta) * pow(2 * A, -1, mod) % mod
    return x1

T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    print(solve_modular_equation(A, B, C))
