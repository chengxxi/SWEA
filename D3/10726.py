# 10726: 이진수 표현

# 10진수에서 2진수로 변환
def todecimal(n):  # n: 0 ~
    ans = ''
    if n == 0:
        ans = '0'
    while n > 0:
        ans += str(n % 2)
        n //= 2

    return ans[::-1]


for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    newM = todecimal(M)

    status = 'OFF'
    length = len(newM)
    checkstatus = newM[length-N:]
    # print(checkstatus)
    if checkstatus == '1' * N:
        status = 'ON'


    print('#{} {}'.format(test_case, status))

'''
정수 N, M 이 주어질 때, M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 판별하여 출력하라.
'''