import math

# 입력 개수를 받습니다.
T = int(input())
# 각 테스트 케이스에 대한 입력을 받습니다.
inputs = [int(input()) for _ in range(T)]
# 결과를 저장할 리스트를 초기화합니다.
results = []

# 각 테스트 케이스에 대해 반복합니다.
for tc in range(1, T + 1):
    # 현재 테스트 케이스의 값을 가져옵니다.
    N = inputs[tc - 1]
    # 이차 방정식의 판별식(discriminant)을 계산합니다.
    discriminant = 8 * N + 1
    # 판별식의 정수 제곱근을 구합니다.
    value = math.isqrt(discriminant)

    # 제곱근의 제곱이 판별식과 같다면 삼각형 층이 가능함을 의미합니다.
    if value * value == discriminant:
        results.append(f"#{tc} {((value - 1) // 2)}")  # 가능한 층 수를 계산하여 결과에 추가합니다.
    else:
        results.append(f"#{tc} -1")  # 불가능한 경우 -1을 결과에 추가합니다.

# 각 테스트 케이스의 결과를 출력합니다.
print("\n".join(results))
