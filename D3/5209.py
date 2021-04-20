# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용 [D3]

def dfs(idx, total):
    global minsum
    if total >= minsum:
        return # pruning

    if idx == n:
        if total < minsum:
            minsum = total
        return # end or array

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1 # mark as visited
            dfs(idx + 1, total + nxn[idx][i])
            visited[i] = 0



for test_case in range(1, int(input())+1):
    n = int(input())
    nxn = [list(map(int, input().split())) for _ in range(n)] # n x n array

    visited = [0] * n # check if visited for each row / col
    minsum = 22500 # 15 * 15 * 100

    dfs(0, 0) # point and total value


    print('#{} {}'.format(test_case, minsum))



'''
A사는 여러 곳에 공장을 갖고 있다. 봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.

각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.

예를 들어 3개의 제품을 생산하려는 경우 각 공장별 생산비용은 다음과 같이 주어진다..


   A  B  C  공장
1  73 21 21
2  11 59 40
3  24 31 83
제품

이때 1-C, 2-A, 3-B로 제품별 생산 공장을 정하면 생산 비용이 21+11+31=63으로 최소가 된다.
'''


'''
cf. SWEA 5189
'''