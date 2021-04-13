# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2

for test_case in range(1, int(input())+1):
    N = float(input()) # decimal num between 0 ~ 1
    decimal = '' # default
    point = 0.5 # 1/(2**1)
    cnt = 0

    while cnt < 13:
        if N == 0:
            break
        elif N < point:
            decimal += '0'
            cnt += 1
        elif N >= point:
            decimal += '1'
            N -= point
            cnt += 1
        point /= 2

    if cnt > 12 or N != 0:
        decimal = 'overflow'



    print('#{} {}'.format(test_case, decimal))



'''
0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.

N = 0.625
0.101 (이진수)
= 1*2-1 + 0*2-2 + 1*2-3
= 0.5 + 0 + 0.125
= 0.625

N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고,
13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.
'''