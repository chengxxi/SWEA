# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리

def bfs(): # start / goal
    while q:
        cur = q.pop(0)

        for j in range(V+1):
            if adj[cur][j] != 0 and distance[j] == 0:
            # 연결되어 있고, (초기 설정된) 거리가 0인 경우
                distance[j] = distance[cur] + 1
                if j == G:
                    return distance[G]
                else:
                    q.append(j)
    return 0 # 다 갔는데 연결 안 되어 있어서 도달 못 함



T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split()) # V: 노드 수 / E: 간선 개수
    edge = [list(map(int, input().split())) for _ in range(E)]

    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for i in range(E): # 인접행
        n1, n2 = edge[i][0], edge[i][1]
        adj[n1][n2] = 1
        adj[n2][n1] = 1


    S, G = map(int, input().split())  # S: 출발 노드 / G: 도착 노드

    q= [S] # queue
    distance = [0] * (V+1)


    print("#{} {}".format(test_case, bfs()))




"""
V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.

주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.

예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.

1     2
| \ / |
4  3  5
|
6

노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.


###  입력  ###
3 # T
----
6 5 # V, E
1 4
1 3
2 3
2 5
4 6
1 6 # S, G
----
7 4 # V, E
1 6
2 3
2 6
3 5
1 5 # S, G
----
9 9 # V, E
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9 # S, G
"""