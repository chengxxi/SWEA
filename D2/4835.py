# 4835: 구간합

T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split())) # 정수 개수 N과 구간의 개수 M
    numbers = list(map(int, input().split()))
   
    values = [] # partsum 저장용 리스트
    for i in range(N-M+1):
        part = numbers[i:i+M] # 구간 slicing해서
        partsum = 0 # 저장할 것인데
        for p in part: # sum이 봉인되어 못 쓰니까 각각 for문 돌려서 저장한다
            partsum += p
        values.append(partsum) # values에 partsum 저장
    
    max_val = min_val = values[0] # max, min을 처음 값으로 초기화
    for val in values:
        if  val > max_val: # max
            max_val = val
        if val < min_val: # min
            min_val = val
    gap = max_val - min_val # gap btw max and min

    print(f"#{test_case} {gap}")            

"""
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
"""