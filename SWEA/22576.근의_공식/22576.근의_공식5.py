def extended_gcd(a, b):
    if b == 0:  # b가 0인 경우 처리
        return abs(a), 1 if a > 0 else -1, 0

    # 재귀 깊이를 제한하기 위해 반복문 사용
    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s * (1 if a > 0 else -1), old_t * (1 if b > 0 else -1)


def safe_mod(a, m):
    try:
        return a % m
    except ZeroDivisionError:
        return -1


def crt(residues, moduli):
    try:
        x = 0
        M = 1
        for modulus in moduli:
            if modulus <= 0:  # 음수 또는 0인 모듈러 처리
                return -1
            M *= modulus

        for residue, modulus in zip(residues, moduli):
            if M > 10 ** 18:  # 너무 큰 수 방지
                return -1
            m = M // modulus
            try:
                g, m_inverse, _ = extended_gcd(m, modulus)
                if g != 1:
                    return -1
                x = safe_mod(x + residue * m * m_inverse, M)
            except (OverflowError, ValueError):
                return -1
        return x
    except Exception:  # 기타 예외 처리
        return -1


def solve_quadratic_mod2k(a, b, c, k):
    if k <= 0:
        return -1
    if k == 1:
        return 0 if c % 2 == 0 else -1

    if a % 2 == b % 2 == 0:
        if c % 2 == 1:
            return -1
        x = solve_quadratic_mod2k(a // 2, b // 2, c // 2, k - 1)
        return -1 if x == -1 else safe_mod(x * 2, 1 << k)

    if a % 2 == 0:
        if b % 2 == 0:
            return -1
        try:
            return safe_mod(-c * pow(b, -1, 1 << k), 1 << k)
        except ValueError:
            return -1

    x = 0
    for i in range(k):
        try:
            px = safe_mod(a * x * x + b * x + c, 1 << (i + 1))
            if px != 0 and safe_mod(a * 2 * x + b, 2) == 1:
                x = safe_mod(x + (1 << i), 1 << k)
        except OverflowError:
            return -1
    return x


def solve_quadratic_mod5k(a, b, c, k):
    if k <= 0:
        return -1
    if k == 1:
        for x in range(5):
            if safe_mod(a * x * x + b * x + c, 5) == 0:
                return x
        return -1

    x = solve_quadratic_mod5k(a, b, c, k - 1)
    if x == -1:
        return -1

    pk = pow(5, k)
    pk_prev = pow(5, k - 1)

    for i in range(5):
        try:
            y = safe_mod(x + i * pk_prev, pk)
            if safe_mod(a * y * y + b * y + c, pk) == 0:
                return y
        except OverflowError:
            continue
    return -1


def solve_quadratic_mod(A, B, C):
    MOD1 = 512  # 2^9
    MOD2 = 1953125  # 5^9
    FINAL_MOD = 10 ** 9

    if not all(isinstance(x, int) for x in (A, B, C)):
        return -1

    if A == 0 and B == 0:
        return 0 if C == 0 else -1

    if A == 0:
        try:
            g1, x1, _ = extended_gcd(B, MOD1)
            if C % g1 != 0:
                return -1
            r1 = safe_mod((-C // g1) * x1, MOD1 // g1)

            g2, x2, _ = extended_gcd(B, MOD2)
            if C % g2 != 0:
                return -1
            r2 = safe_mod((-C // g2) * x2, MOD2 // g2)

            mod1_adjusted = MOD1 // g1
            mod2_adjusted = MOD2 // g2

            result = crt([r1, r2], [mod1_adjusted, mod2_adjusted])
            return safe_mod(result, FINAL_MOD)
        except Exception:
            return -1

    x1 = solve_quadratic_mod2k(A, B, C, 9)
    x2 = solve_quadratic_mod5k(A, B, C, 9)

    if x1 == -1 or x2 == -1:
        return -1

    result = crt([x1, x2], [MOD1, MOD2])
    return safe_mod(result, FINAL_MOD)


def main():
    T = int(input())
    for _ in range(T):
        A, B, C = map(int, input().split())
        result = solve_quadratic_mod(A, B, C)
        if result < 0 or result >= 10 ** 9:
            result = -1
        # 검산: A * x^2 + B * x + C가 유효한지 확인
        if result != -1 and (A * result ** 2 + B * result + C) % (10 ** 9) != 0:
            result = -1
        print(result)


if __name__ == "__main__":
    main()
