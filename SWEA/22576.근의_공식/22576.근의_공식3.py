def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y


def crt(residues, moduli):
    x = 0
    M = 1
    for modulus in moduli:
        M *= modulus
    for residue, modulus in zip(residues, moduli):
        m = M // modulus
        g, m_inverse, _ = extended_gcd(m, modulus)
        if g != 1:
            return -1
        x = (x + residue * m * m_inverse) % M
    return x


def solve_quadratic_mod2k(a, b, c, k):
    """2의 거듭제곱 모듈로에서 이차방정식 해결"""
    if k == 1:
        # mod 2에서는 모든 수가 제곱수
        return 0 if c % 2 == 0 else -1

    if a % 2 == b % 2 == 0:
        if c % 2 == 1:
            return -1
        # 방정식을 2로 나누고 재귀적으로 해결
        x = solve_quadratic_mod2k(a // 2, b // 2, c // 2, k - 1)
        return -1 if x == -1 else (x * 2)

    if a % 2 == 0:
        # bx ≡ -c (mod 2^k)
        if b % 2 == 0:
            return -1
        return (-c * pow(b, -1, 1 << k)) % (1 << k)

    # Hensel lifting for odd a
    x = 0
    for i in range(k):
        px = (a * x * x + b * x + c) % (1 << (i + 1))
        if px != 0:
            if (a * 2 * x + b) % 2 == 1:
                x += 1 << i
    return x


def solve_quadratic_mod5k(a, b, c, k):
    """5의 거듭제곱 모듈로에서 이차방정식 해결"""
    if k == 1:
        # mod 5에서 완전탐색
        for x in range(5):
            if (a * x * x + b * x + c) % 5 == 0:
                return x
        return -1

    x = solve_quadratic_mod5k(a, b, c, k - 1)
    if x == -1:
        return -1

    pk = 5 ** k
    pk_prev = 5 ** (k - 1)

    for i in range(5):
        y = x + i * pk_prev
        if (a * y * y + b * y + c) % pk == 0:
            return y

    return -1


def solve_quadratic_mod(A, B, C):
    MOD1 = 512  # 2^9
    MOD2 = 1953125  # 5^9

    if A == 0:
        if B == 0:
            return 0 if C == 0 else -1
        # 선형 방정식 해결
        g1, x1, _ = extended_gcd(B, MOD1)
        g2, x2, _ = extended_gcd(B, MOD2)
        if C % g1 or C % g2:
            return -1
        r1 = (-C * x1) % MOD1
        r2 = (-C * x2) % MOD2
        return crt([r1, r2], [MOD1, MOD2])

    # 2^9와 5^9에 대해 각각 해결
    x1 = solve_quadratic_mod2k(A, B, C, 9)
    x2 = solve_quadratic_mod5k(A, B, C, 9)

    if x1 == -1 or x2 == -1:
        return -1

    return crt([x1, x2], [MOD1, MOD2])

def valid_test(A, B, C, x):
    return (A * x**2 + B * x + C)// (10 ** 9)

def main():
    T = int(input())
    for _ in range(T):
        A, B, C = map(int, input().split())
        result = solve_quadratic_mod(A, B, C)
        print(result)
        print(valid_test(A, B, C, result))


if __name__ == "__main__":
    main()