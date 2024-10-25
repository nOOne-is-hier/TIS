def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def safe_mod(a, m):
    if m <= 0:
        return -1
    return a % m


def find_all_solutions(A, B, C, M):
    """모든 가능한 해를 찾는 함수"""
    solutions = set()

    # 계수들의 GCD 계산
    g = gcd(gcd(abs(A) if A else abs(B), abs(C) if C else M), M)

    if g > 1:
        # 공통 인수로 나누어 단순화
        A, B, C = A // g, B // g, C // g
        M = M // g

        # 단순화된 방정식의 해를 찾음
        temp_solutions = find_all_solutions(A, B, C, M)

        # 원래 모듈러로 변환하고 모든 가능한 해 추가
        for x in temp_solutions:
            for i in range(g):
                new_x = x + i * M
                if new_x < 10 ** 9:
                    solutions.add(new_x)
                else:
                    break
    else:
        # 기본 케이스: 직접 해 찾기
        for x in range(M):
            if (A * x * x + B * x + C) % M == 0:
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
    if len(residues) != len(moduli):
        return -1

    total = 0
    product = 1
    for modulus in moduli:
        product *= modulus

    for residue, modulus in zip(residues, moduli):
        p = product // modulus
        g, inv, _ = extended_gcd(p, modulus)

        if g != 1:  # 모듈러가 서로소가 아닌 경우
            # 공통 인수로 나누어 처리
            d = gcd(modulus, p)
            if residue % d != (total % modulus) % d:
                return -1
            # 새로운 모듈러와 나머지로 계산
            new_modulus = modulus // d
            new_residue = residue % new_modulus
            new_p = p // d
            _, inv, _ = extended_gcd(new_p, new_modulus)
            total = safe_mod(total + new_residue * new_p * inv, product)
        else:
            total = safe_mod(total + residue * p * inv, product)

    return total


def solve_quadratic_mod(A, B, C):
    MOD1 = 512  # 2^9
    MOD2 = 1953125  # 5^9
    FINAL_MOD = 10 ** 9

    if A == 0 and B == 0:
        return 0 if C == 0 else -1

    # 전체 방정식의 GCD 계산
    g = gcd(gcd(abs(A) if A else abs(B), abs(C) if C else FINAL_MOD), FINAL_MOD)

    if g > 1:
        # 방정식을 GCD로 나누어 단순화
        A, B, C = A // g, B // g, C // g
        temp_solutions = solve_quadratic_mod(A, B, C)
        if temp_solutions == -1:
            return -1

        # 원래 모듈러로 변환하여 가장 작은 해 찾기
        solutions = set()
        for i in range(g):
            new_sol = temp_solutions + i * (FINAL_MOD // g)
            if new_sol < FINAL_MOD:
                solutions.add(new_sol)

        return min(solutions) if solutions else -1

    # 2진 및 5진 해 찾기
    solutions = set()

    x1 = solve_quadratic_mod2k(A, B, C, 9)
    x2 = solve_quadratic_mod5k(A, B, C, 9)

    if x1 != -1 and x2 != -1:
        result = crt([x1, x2], [MOD1, MOD2])
        if result != -1 and result < FINAL_MOD:
            solutions.add(result)

    # 개별 모듈러에 대한 해도 검토
    if x1 != -1:
        solutions.add(x1)
    if x2 != -1:
        solutions.add(x2)

    # 모든 해 검증
    valid_solutions = set()
    for x in solutions:
        if 0 <= x < FINAL_MOD and (A * x * x + B * x + C) % FINAL_MOD == 0:
            valid_solutions.add(x)

    return min(valid_solutions) if valid_solutions else -1


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
