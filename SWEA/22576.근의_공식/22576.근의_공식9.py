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


def find_all_solutions(A, B, C, M):
    """모든 가능한 해를 찾는 함수"""
    solutions = set()

    # A, B가 모두 0인 특수한 경우 처리
    if A == 0 and B == 0:
        if C == 0:
            # 모든 x가 해가 됨
            return {0}  # 가장 작은 해만 반환
        elif C % M == 0:
            return {0}
        else:
            return set()

    # A가 0인 선형 방정식의 경우
    if A == 0:
        # Bx ≡ -C (mod M)
        g = gcd(abs(B), M)
        if C % g != 0:
            return set()
        # 방정식을 g로 나누어 단순화
        b, m = B // g, M // g
        c = -(C // g)
        # b의 역원을 구함
        _, b_inv, _ = extended_gcd(b, m)
        x0 = (b_inv * c) % m
        # 모든 해를 생성
        for i in range(g):
            new_x = x0 + i * m
            if new_x < M:
                solutions.add(new_x)
        return solutions

    # 계수들의 GCD 계산
    g = gcd(gcd(abs(A), abs(B) if B else M), abs(C) if C else M)

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
        # 평방근 고려
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
    x = 0
    M = 1

    # M 계산 (모든 모듈러의 곱)
    for modulus in moduli:
        if modulus <= 0:
            return -1
        M *= modulus

    for mi, residue in zip(moduli, residues):
        Mi = M // mi
        _, inv, _ = extended_gcd(Mi, mi)
        x = (x + residue * Mi * inv) % M

    return x


def solve_quadratic_mod(A, B, C):
    MOD1 = 512  # 2^9
    MOD2 = 1953125  # 5^9
    FINAL_MOD = 10 ** 9

    # 특수 케이스: 모든 계수가 0인 경우
    if A == 0 and B == 0 and C == 0:
        return 0

    # 선형 방정식 케이스
    if A == 0:
        if B == 0:
            return 0 if C == 0 else -1
        # Bx ≡ -C (mod FINAL_MOD)
        g = gcd(abs(B), FINAL_MOD)
        if C % g != 0:
            return -1
        b, m = B // g, FINAL_MOD // g
        c = -(C // g)
        _, b_inv, _ = extended_gcd(b, m)
        x0 = (b_inv * c) % m
        return x0

    # 전체 방정식의 GCD 계산
    g = gcd(gcd(abs(A), abs(B) if B else FINAL_MOD), abs(C) if C else FINAL_MOD)

    if g > 1:
        # 방정식을 GCD로 나누어 단순화
        A, B, C = A // g, B // g, C // g
        temp_solution = solve_quadratic_mod(A, B, C)
        if temp_solution == -1:
            return -1
        return temp_solution

    # 2진 및 5진 해 찾기
    x1 = solve_quadratic_mod2k(A, B, C, 9)
    x2 = solve_quadratic_mod5k(A, B, C, 9)

    if x1 == -1 or x2 == -1:
        return -1

    # CRT로 해 결합
    result = crt([x1, x2], [MOD1, MOD2])

    # 결과 검증
    if result >= 0 and result < FINAL_MOD:
        if (A * result * result + B * result + C) % FINAL_MOD == 0:
            return result

    return -1


def main():
    T = int(input())
    for _ in range(T):
        A, B, C = map(int, input().split())
        result = solve_quadratic_mod(A, B, C)
        if result < 0 or result >= 10 ** 9:
            result = -1
        # 검산: A * x^2 + B * x + C가 유효한지 확인
        if result != -1 and (A * result * result + B * result + C) % (10 ** 9) != 0:
            result = -1
        print(result)


if __name__ == "__main__":
    main()