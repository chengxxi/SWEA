# 2071. 평균값 구하기

num = int(input())
for n in range(num):
    total = 0; avg = 0
    numbers = list(map(int, input().split()))
    for i in numbers:
        total += i
    avg = int(round(total / len(numbers), 0))
    print("#{} {}".format(n+1,avg))

"""
10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

(소수점 첫째 자리에서 반올림한 정수를 출력한다.)
"""