# 1954: 달팽이 숫자

T = int(input())
for test_case in range(1, T + 1):
    # 달팽이집 만들기
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)] 
    
    # 패턴 확인, 반복하기
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    x = 0; y = 0; d = 0
    arr[x][y] = 1 # 맨 처음 값 설정
    num = 2
    
    while num <= N*N: # num : 1 ~ N^2
        # 모서리에 닿으면 방향 전환
        if 0 <= x + dr[d%4] < N and 0 <= y + dc[d%4] < N and arr[x + dr[d%4]][y + dc[d%4]] == 0:
            x = x + dr[d%4]
            y = y + dc[d%4]
            arr[x][y] = num
            num += 1
        else:
            d += 1

    
    print("#{}".format(test_case))
    
    for nlist in arr: 
        print(*nlist)


"""
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

** 방향 변경 조건 : 행렬의 끝에 도달 or value already exists


https://itzjamie96.github.io/2020/11/18/swea-python-1954/
"""