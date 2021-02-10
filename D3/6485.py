# 6485. 삼성시의 버스 노선

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    stops = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())

        for j in range(A, B+1):
            stops[j] += 1
    
    print("#{}".format(tc), end=" ")


    P = int(input())
    for i in range(P):
        C = int(input())
        print(stops[C], end=" ")
    
    print( )

 

"""
삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 번호가 붙어 있다.

그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,

Bi이하인 모든 정류장만을 다니는 버스 노선이다.

P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.
"""
