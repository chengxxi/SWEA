# 4828: min max

T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    numbers = list(map(int, input().split()))
    max_num = numbers[0]; min_num = numbers[0]
    for n in numbers:
        if n >= max_num:
            max_num = n
        if n <= min_num:
            min_num = n
    gap = abs(max_num - min_num)
    print("#{} {}".format(test_case, gap))


"""
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
"""