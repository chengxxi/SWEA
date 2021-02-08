# 1976. 시각 덧셈

T = int(input())
for test_case in range(1, T + 1):
    h1, m1, h2, m2 = list(map(int, input().split()))
    hour = h1 + h2
    minute = m1+m2
    if minute >= 60:
        minute -= 60
        hour += 1
    if hour > 12:
        hour -= 12
    print(f"#{test_case} {hour} {minute}")
    

"""
시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.

(시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)
"""