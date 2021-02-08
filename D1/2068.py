# 2068. 최대수 구하기

num = int(input())
for i in range(num):
    nums = list(map(int, input().split()))
    print("#{} {}".format(i+1, max(nums)))
    
"""
10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
"""