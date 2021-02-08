# 1933. 간단한 N 의 약수

num = int(input())
for n in range(1, num+1):
    if num % n == 0:
        print(n, end=' ')

"""
입력으로 1개의 정수 N 이 주어진다.

정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
"""