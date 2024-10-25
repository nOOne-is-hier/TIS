def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# safe_mod 함수는 필요하지 않음: Python의 정수는 overflow로부터 자유롭기 때문
# 따라서 큰 수를 다루는 연산도 그대로 수행 가능


def safe_mod(a, m):
    if m <= 0:
        return -1
    return a % m


def crt(residues, moduli):
    x = 0
    M = 1

    # M 계산 (모든 모듈러의 곱)
    for modulus in moduli:
        if modulus <= 0:  # 음수 또는 0인 모듈러 처리
            return -1
        M *= modulus

    for residue, modulus in zip(residues, moduli):
        m = M // modulus
        g, m_inverse, _ = extended_gcd(m, modulus)
        if g != 1:
            # 모듈러가 서로소가 아니면 해를 찾을 수 있는지 확인
            if residue % g != 0:
                return -1  # 해가 존재하지 않음
            # 서로소가 아닌 경우, 공통 인수로 나눈 뒤 문제를 다시 설정
            modulus //= g
            residue //= g
            m_inverse = extended_gcd(m // g, modulus)[1]  # 새로운 모듈러에 대한 역원 계산
        # m_inverse는 m * m_inverse ≡ 1 (mod modulus)를 만족하는 값
        x = (x + residue * m * m_inverse) % M

    # 모든 가능한 경우에 대해 해를 찾음
    possible_solutions = [x]
    for residue, modulus in zip(residues, moduli):
        new_solutions = []
        for solution in possible_solutions:
            for i in range(g):
                candidate = (solution + i * (M // modulus)) % M
                if candidate >= 0 and all((candidate % mod == res % mod) for res, mod in zip(residues, moduli)):
                    new_solutions.append(candidate)
        possible_solutions = new_solutions if new_solutions else possible_solutions

    return min(possible_solutions) if possible_solutions else -1


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
