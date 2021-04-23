# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용 [D3]

### Dijkstra algorithm ###

def dijkstra(i, j):
    inf = 10000
    D = [[inf] * n for _ in range(n)]
    D[0][0] = 0 # start point
    queue = [[i, j]]

    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    while queue:
        ci, cj = queue.pop(0)

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]

            if 0 <= ni < n and 0 <= nj < n:
                dif = nxn[ni][nj] - nxn[ci][cj] if nxn[ni][nj] > nxn[ci][cj] else 0
                cost = D[ci][cj] + dif + 1 # start point

                if D[ni][nj] > cost:
                    D[ni][nj] = cost
                    queue.append([ni, nj])


    return D[n-1][n-1]




for test_case in range(1, int(input())+1):
    n = int(input())
    nxn = [list(map(int, input().split())) for _ in range(n)] # heights

    answer = dijkstra(0, 0)


    print('#{} {}'.format(test_case, answer))



'''
출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라지기 때문에, 최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.

다음은 각 지역의 높이를 기록한 표의 예로, 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래이며, 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.

(표에 표시되지 않은 지역이나 대각선 방향으로는 이동 불가.)

0 2 1
0 1 1
1 1 1

인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고, 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다.

(0)  2   1
(0)  1   1
(1) (1) (1)


색이 칠해진 칸을 따라 이동하는 경우 기본적인 연료 소비량 4에, 높이가 0에서 1로 경우만큼 추가 연료가 소비되므로 최소 연료 소비량 5로 목적지에 도착할 수 있다.

이동 가능한 지역의 높이 정보에 따라 최소 연료 소비량을 출력하는 프로그램을 만드시오.
'''
