# FA (14935)
# https://www.acmicpc.net/problem/14935

import sys

# def recursive(x, prev = []):
#     if len(prev) == 0:
#         prev.append(x)

#     if x == prev[0]:
#         return True
    
#     prev[0] = x
#     recursive(str(x[0] * len(x)))

def main() -> None:
    # 입력 최적화
    sys.stdin = open("input.txt", "r")
    input = sys.stdin.readline

    x = input()
    print("FA")

    # for i in range(100000000, 0, -1):
    #     if recursive(str(i)):
    #         print(f"{i} FA")

    # i = 231860431313212318640321643213743164031321684311684351321567432165101567893214638976459864597864
    # if recursive(str(i)):
    #     print(f"{i} FA")
        

if __name__ == "__main__":
    main()
