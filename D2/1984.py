# 1984. 중간 평균값 구하기

T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    maxn =num[0]
    minn = num[0]
    for n in range(len(num)):
        if maxn <= num[n]:
            maxn = num[n]
        if minn >= num[n]:
            minn = num[n]
    num.remove(maxn)
    num.remove(minn)
    avg = sum(num)/8
    print("#{} {}".format(test_case, round(avg)))

"""
10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.

(소수점 첫째 자리에서 반올림한 정수를 출력한다.)
"""