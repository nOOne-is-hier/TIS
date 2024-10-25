import math


def gcd(a, b):
    return math.gcd(a, b)


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def safe_mod_multiply(a, b, mod):
    return ((a % mod) * (b % mod)) % mod


def tonelli_shanks(n, p):
    if pow(n, (p - 1) // 2, p) != 1:
        return -1

    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)

    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1

    z = 2
    while pow(z, (p - 1) // 2, p) == 1:
        z += 1

    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)

    while t != 0 and t != 1:
        t2i = t
        i = 0
        for i in range(1, m):
            t2i = (t2i * t2i) % p
            if t2i == 1:
                break

        if i == m:
            return -1

        b = pow(c, 1 << (m - i - 1), p)
        m = i
        c = (b * b) % p
        t = (t * b * b) % p
        r = (r * b) % p

    return r if t == 1 else -1


def find_all_solutions(A, B, C, M):
    solutions = set()

    if A == 0 and B == 0:
        if C == 0 or C % M == 0:
            return {0}
        return set()

    if A == 0:
        g = gcd(abs(B), M)
        if C % g != 0:
            return set()

        b, m = B // g, M // g
        c = -(C // g)
        _, b_inv, _ = extended_gcd(b, m)
        x0 = (b_inv * c) % m

        for i in range(g):
            solutions.add((x0 + i * m) % M)
        return solutions

    g = gcd(gcd(abs(A), abs(B) if B else M), abs(C) if C else M)

    if g > 1:
        A, B, C = A // g, B // g, C // g
        M = M // g

        temp_solutions = find_all_solutions(A, B, C, M)

        for x in temp_solutions:
            for i in range(g):
                new_x = (x + i * M) % (M * g)
                if new_x < 10 ** 9:
                    solutions.add(new_x)
        return solutions

    if B == 0:
        if M > 1 and M % 2 == 1:
            try:
                A_inv = pow(A, -1, M)
                n = (-C * A_inv) % M
                r = tonelli_shanks(n, M)
                if r != -1:
                    solutions.add(r)
                    solutions.add(M - r)
            except ValueError:
                pass
        else:
            for x in range(M):
                if (safe_mod_multiply(A * x % M, x, M) + C) % M == 0:
                    solutions.add(x)
    else:
        for x in range(M):
            if (safe_mod_multiply(A * x % M, x, M) + B * x + C) % M == 0:
                solutions.add(x)

    return solutions


def solve_quadratic_mod2k(a, b, c, k):
    if k <= 0:
        return -1

    mod = 1 << k
    solutions = find_all_solutions(a, b, c, mod)
    return min(solutions) if solutions else -1


def solve_quadratic_mod5k(a, b, c, k):
    if k <= 0:
        return -1

    mod = pow(5, k)
    solutions = find_all_solutions(a, b, c, mod)
    return min(solutions) if solutions else -1


def crt(residues, moduli):
    x = 0
    M = 1

    for modulus in moduli:
        if modulus <= 0:
            return -1
        M *= modulus

    for residue, modulus in zip(residues, moduli):
        m = M // modulus
        g, m_inverse, _ = extended_gcd(m, modulus)

        if g != 1:
            return -1

        x = (x + residue * m * m_inverse) % M

    return x


def solve_quadratic_mod(A, B, C):
    MOD1 = 512
    MOD2 = 1953125
    FINAL_MOD = 10 ** 9

    if A == 0 and B == 0:
        return 0 if C == 0 or C % FINAL_MOD == 0 else -1

    if A == 0:
        g = gcd(abs(B), FINAL_MOD)
        if C % g != 0:
            return -1

        b, m = B // g, FINAL_MOD // g
        c = -(C // g)
        _, b_inv, _ = extended_gcd(b, m)
        return (b_inv * c) % FINAL_MOD

    g = gcd(gcd(abs(A), abs(B)), abs(C))
    if g > 1:
        A, B, C = A // g, B // g, C // g
        temp_solution = solve_quadratic_mod(A, B, C)
        if temp_solution == -1:
            return -1
        return temp_solution

    x1 = solve_quadratic_mod2k(A, B, C, 9)
    if x1 == -1:
        return -1

    x2 = solve_quadratic_mod5k(A, B, C, 9)
    if x2 == -1:
        return -1

    result = crt([x1, x2], [MOD1, MOD2])

    if 0 <= result < FINAL_MOD:
        if (A * result * result + B * result + C) % FINAL_MOD == 0:
            return result

    return -1


def main():
    T = int(input())
    for _ in range(T):
        A, B, C = map(int, input().split())
        result = solve_quadratic_mod(A, B, C)
        print(result)


if __name__ == "__main__":
    main()
