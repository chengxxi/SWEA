T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split()) # K :  1회 충전 시 주행 가능한 거리 / N : 전체 거리의 길이 / M : 충전기가 설치된 stop 수
    stops = list(map(int, input().split()))
    
    elec = [0] * (N+1) # 0 ~ N의 길이만큼 전체 거리 생성
    for stop in range(N):
        if stop in stops:
            elec[stop] += 1 # 충전기가 있으면 1, 아니면 0
    
    point = 0; far = K; count = 0 
    # 각각 처음 시작하는 point와 point에서 어떤 거리만큼 떨어져 있는 far, 그리고 충전횟수 charge
    while far < N:
        for st in range(0, M-1): # M개의 충전기에 대하여,
            gap = stops[st+1] - stops[st]
        if gap > K:
            charge = 0 # 도착할 수 없는 경우
            break
        else:
            for i in range(point+1, gap+1):
                if elec[i] == 1:
                    point = i
            count += 1
            far = point + K
                    
    print(f"#{test_case} {charge}")
        
    