# 1948. 날짜 계산기

T = int(input())
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = list(map(int, input().split()))
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m1 == m2:
        day = d2 - d1 + 1
    else:
        day = days[m1 - 1] - d1 + 1 # m1에서 남은 날 더하기
        day += d2 # m2의 날 수 더하기
        for i in range(m1 + 1, m2):
            day += days[i-1] # m1 + 1 ~ m2 - 1 달 사이의 날들 더하기
    print(f"#{test_case} {day}")
                
          
"""
월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.
"""