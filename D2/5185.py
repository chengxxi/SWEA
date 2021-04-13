#  5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# 10진수에서 2진수로 변환
def todecimal(n): # n: 0 ~ 15
    ans = ''
    while n > 0:
        ans += str(n%2)
        n //= 2

    # 자릿수 맞추는 용도
    if len(ans) == 3:
        ans += '0'
    if len(ans) == 2:
        ans += '00'
    if len(ans) == 1:
        ans += '000'

    return ans[::-1]


for test_case in range(1, int(input())+1):
    N, hexa = input().split()
    decimal_str = ''
    # for char in hexa:

    # text to number using index (0 ~ 15)
    for i in range(len(hexa)):
        char = list(hexa)[i]
        num = hexadecimal.index(char)
        decimal = todecimal(num)
        if num == 0:
            decimal_str += '0000'
        # 2차원의 숫자로 이어붙이기
        decimal_str += decimal


    print('#{} {}'.format(test_case, decimal_str))



'''
16진수 1자리는 2진수 4자리로 표시된다.

N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.

단, 2진수의 앞자리 0도 반드시 출력한다.

예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.

0100011111111110
'''