# 1970. 거스름돈


for test_case in range(1, int(input())+1):
    monetary = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money = int(input())

    change = [0] * 8

    for i in range(8): # moneraty
        if money // monetary[i] > 0:
            change[i] += money // monetary[i]
            money = money % monetary[i]

    print('#{}'.format(test_case))
    print(*change)



'''
우리나라 화폐 ‘원’은 금액이 높은 돈을 우선적으로 계산할 때 돈의 개수가 가장 최소가 된다.

S마켓에서 사용하는 돈의 종류는 다음과 같다.
50,000 원
10,000 원
5,000 원
1,000 원
500 원
100 원
50 원
10 원
'''