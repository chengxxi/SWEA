# 1986. 지그재그 숫자

T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    answer = 0
    for n in range(1, num+1):
        if n % 2 == 0:
            answer -= n
        else:
            answer += n
    print(f"#{test_case} {answer}")

"""
1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.
"""