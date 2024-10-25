def gcd(a, b):
    # 유클리드 호제법을 이용하여 최대공약수(GCD)를 계산하는 함수
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    # 확장 유클리드 호제법을 이용하여 최대공약수와 (x, y)를 구하는 함수
    # a * x + b * y = gcd(a, b)를 만족하는 (x, y)를 찾음
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def tonelli_shanks(n, p):
    """Tonelli-Shanks algorithm to find square root of n modulo p.
    Returns a solution x such that x^2 ≡ n (mod p), or -1 if no solution exists.
    """
    assert pow(n, (p - 1) // 2, p) == 1, "No solution exists for n mod p"

    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)

    # Factor p - 1 as q * 2^s
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1

    # Find a non-residue z
    z = 2
    while pow(z, (p - 1) // 2, p) == 1:
        z += 1

    # Initialize values
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)

    while t != 0 and t != 1:
        # Find the lowest i such that t^(2^i) ≡ 1 (mod p)
        t2i = t
        i = 0
        for i in range(1, m):
            t2i = pow(t2i, 2, p)
            if t2i == 1:
                break

        # Update values
        b = pow(c, 1 << (m - i - 1), p)
        m = i
        c = (b * b) % p
        t = (t * b * b) % p
        r = (r * b) % p

    return r if t == 1 else -1


def find_all_solutions(A, B, C, M):
    """모든 가능한 해를 찾는 함수
    A * x^2 + B * x + C ≡ 0 (mod M)인 모든 해를 구함
    """
    solutions = set()

    # A, B가 모두 0인 특수한 경우 처리
    if A == 0 and B == 0:
        if C == 0 or C % M == 0:
            return {0}  # 모든 x에 대해 해가 존재함
        return set()  # 해가 존재하지 않음

    # A가 0인 선형 방정식의 경우
    if A == 0:
        # B * x ≡ -C (mod M)
        g = gcd(abs(B), M)

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

    # 전체 방정식의 GCD 계산
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
        # 완전 제곱식 확인
        if B == 0:
            # A * x^2 + C ≡ 0 (mod M)
            if M > 1 and M % 2 == 1:  # M이 소수일 때 Tonelli-Shanks 알고리즘 적용 가능
                solution = tonelli_shanks(-C * pow(A, -1, M), M)
                if solution != -1:
                    solutions.add(solution)
                    solutions.add(M - solution)  # 두 개의 해가 존재할 수 있음
            else:
                for x in range(M):
                    if (A * x * x + C) % M == 0:
                        solutions.add(x)
        else:
            # 일반적인 이차방정식
            for x in range(M):
                if (A * x * x + B * x + C) % M == 0:
                    solutions.add(x)

    return solutions


def solve_quadratic_mod2k(a, b, c, k):
    # 모듈러 2^k에서의 이차방정식 해 찾기
    if k <= 0:
        return -1

    mod = 1 << k  # 2^k 계산
    solutions = find_all_solutions(a, b, c, mod)
    return min(solutions) if solutions else -1


def solve_quadratic_mod5k(a, b, c, k):
    # 모듈러 5^k에서의 이차방정식 해 찾기
    if k <= 0:
        return -1

    mod = pow(5, k)  # 5^k 계산
    solutions = find_all_solutions(a, b, c, mod)
    return min(solutions) if solutions else -1


def crt(residues, moduli):
    # 중국인의 나머지 정리(CRT)를 이용하여 일치하는 값을 찾는 함수
    x = 0
    M = 1

    # 모든 모듈러의 곱 계산
    for modulus in moduli:
        if modulus <= 0:  # 음수 또는 0인 모듈러 처리
            return -1
        M *= modulus

    for residue, modulus in zip(residues, moduli):
        m = M // modulus
        g, m_inverse, _ = extended_gcd(m, modulus)
        if g != 1:

            modulus //= g
            residue //= g
            m //= g
            m_inverse = extended_gcd(m, modulus)[1]  # 새로운 모듈러에 대한 역원 계산
        # m_inverse는 m * m_inverse ≡ 1 (mod modulus)를 만족하는 값
        x = (x + residue * m * m_inverse) % M

    return x


def solve_quadratic_mod(A, B, C):
    # 최종적으로 10^9 모듈러에서 이차방정식 해 찾기
    MOD1 = 512  # 2^9
    MOD2 = 1953125  # 5^9
    FINAL_MOD = 10 ** 9

    # 특수 케이스들 처리
    if A == 0 and B == 0:
        return 0 if C == 0 or C % FINAL_MOD == 0 else -1

    if A == 0:
        if B == 0:
            return -1
        # 선형 방정식 처리
        g = gcd(abs(B), FINAL_MOD)

        b, m = B // g, FINAL_MOD // g
        c = -(C // g)
        _, b_inv, _ = extended_gcd(b, m)
        x0 = (b_inv * c) % m
        return x0

    # 전체 방정식의 GCD 계산 후 단순화
    g = gcd(gcd(abs(A), abs(B)), abs(C))
    if g > 1:
        A, B, C = A // g, B // g, C // g
        FINAL_MOD = FINAL_MOD // g  # 수정된 부분
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
    # 입력 받기 및 해 찾기
    T = int(input())  # 테스트 케이스 수
    for _ in range(T):
        A, B, C = map(int, input().split())  # 계수 A, B, C 입력 받기
        result = solve_quadratic_mod(A, B, C)
        # 검산
        if result != -1 and (A * result * result + B * result + C) % (10 ** 9) != 0:
            result = -1  # 검산 실패 시 결과를 -1로 설정
        print(result)  # 결과 출력


if __name__ == "__main__":
    main()
