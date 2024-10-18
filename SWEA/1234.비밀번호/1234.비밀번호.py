import sys

sys.stdin = open('input.txt')
# 1. 스택을 이용한 방법
'''for tc in range(1, 11):
    length, fake_password = input().split()
    password = []

    for number in fake_password:
        if password and password[-1] == number:
            password.pop()
        else:
            password.append(number)

    print(f'#{tc} {"".join(password)}')'''

# 2. 스택을 이용한 방법2
'''for tc in range(1, 11):
    arr = input().split()
    stack = []

    for num in arr[1]:
        if not stack:
            stack.append(num)
        else:
            if num == stack[-1]:
                stack.pop()
            else:
                stack.append(num)'''

# 3. 문자열 메서드와 재귀 함수를 이용한 방법, for loop
'''def decryption(code):
    for idx in range(len(code)-1):
        if code[idx] == code[idx+1]:
            code = code.replace(code[idx]*2, '', 1)
            return decryption(code)
    return code


for tc in range(1, 11):
    length, fake_password = input().split()
    print(f'#{tc}', decryption(fake_password))'''

# 4. 문제열 메서드를 이용한 방법, while loop
for tc in range(1, 11):
    length, fake_password = input().split()
    idx = 1
    while idx < len(fake_password):

        if fake_password[idx-1] == fake_password[idx]:
            fake_password = fake_password.replace(fake_password[idx]*2, '', 1)
            idx -= 1
        else:
            idx += 1

    print(f'#{tc}', fake_password)