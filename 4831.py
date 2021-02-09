# 4831: 전기버스

T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split()) # K :  1회 충전 시 주행 가능한 거리 / N : 전체 거리의 길이 / M : 충전기가 설치된 stop 수
    stops = list(map(int, input().split()))
    
    elec = [0] * (N+1) # 0 ~ N의 길이만큼 전체 거리 생성
    for stop in range(N):
        if stop in stops:
            elec[stop] += 1 # 충전기가 있으면 1, 아니면 0
    
    point = 0; end = K; charge= 0
    # 각각 처음 시작하는 point와 point에서 어떤 거리만큼 떨어져 있는 far, 그리고 충전횟수 charge
    while True:
        zero = 0
        for i in range(point+1, end+1):
            if elec[i] == 1:
                point = i
            else:
                zero += 1
                
        if zero == K:
            charge = 0
            break
            
        charge += 1
        end = point + K
        
        if end >= N:
            break
    
    print(f"#{test_case} {charge}")


"""
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
"""


# T = int(input())
# for test_case in range(1, T + 1):
#     K, N, M = map(int, input().split()) # K :  1회 충전 시 주행 가능한 거리 / N : 전체 거리의 길이 / M : 충전기가 설치된 stop 수
#     stops = list(map(int, input().split()))
    
#     elec = [0] * (N+1) # 0 ~ N의 길이만큼 전체 거리 생성
#     for stop in range(N):
#         if stop in stops:
#             elec[stop] += 1 # 충전기가 있으면 1, 아니면 0
    
#     point = 0; far = K; count = 0 
#     # 각각 처음 시작하는 point와 point에서 어떤 거리만큼 떨어져 있는 far, 그리고 충전횟수 charge
#     while far < N:
#         for st in range(0, M-1): # M개의 충전기에 대하여,
#             gap = stops[st+1] - stops[st]
#         if gap > K:
#             charge = 0 # 도착할 수 없는 경우
#             break
#         else:
#             for i in range(point+1, gap+1):
#                 if elec[i] == 1:
#                     point = i
#             count += 1
#             far = point + K
                    
#     print(f"#{test_case} {charge}")
        
    