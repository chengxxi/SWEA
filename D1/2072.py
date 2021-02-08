# 2072. 홀수만 더하기

T = int(input())
for t in range(1, T + 1):
    test_case = list(map(int, input().split()))
    total = 0
    for i in test_case:
        if i % 2:
            total += i
    print("#{} {}".format(t, total))

"""
10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
"""