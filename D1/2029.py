# 2029. 몫과 나머지 출력하기

num = int(input())
for n in range(1, num+1):
    a, b = list(map(int, input().split()))
    print("#{} {} {}".format(n, a//b, a%b))

"""
2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.
"""