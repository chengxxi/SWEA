# 2070. 큰 놈, 작은 놈, 같은 놈

N = int(input())
for i in range(N):
    a, b = list(map(int, input().split()))
    if a > b:
        print('#{} >'.format(i+1))
    elif a == b:
        print('#{} ='.format(i+1))
    elif a < b:
        print('#{} <'.format(i+1))
        
"""
2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
"""