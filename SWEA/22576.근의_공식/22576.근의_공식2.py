import sys
sys.stdin = open('input.txt')
def mod_solve(T, cases):
    MOD = 10 ** 9
    results = []

    for case in cases:
        A, B, C = case

        if A == 0:
            if B == 0:
                if C == 0:
                    results.append(0)  # 모든 x에 대해 성립
                else:
                    results.append(-1)  # 해가 없음
            else:
                # Bx + C ≡ 0 (mod 10^9) -> x ≡ -C / B (mod 10^9)
                if B % MOD == 0:
                    results.append(-1)
                else:
                    x = (-C % MOD) * pow(B, -1, MOD) % MOD
                    results.append(x)
        else:
            # A가 0이 아닌 경우, 이차 방정식을 풀어야 함
            found = False
            for x in range(MOD):
                if (A * x * x + B * x + C) % MOD == 0:
                    results.append(x)
                    found = True
                    break
            if not found:
                results.append(-1)  # 해가 없음

    return results

# 입력 처리
T = int(input())  # 테스트 케이스 수
cases = [tuple(map(int, input().split())) for _ in range(T)]  # 테스트 케이스들 입력

# 결과 출력
results = mod_solve(T, cases)
for res in results:
    print(res)
