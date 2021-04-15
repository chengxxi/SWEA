#  5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

def dfs(y, x, total):
    global min_usage

    if total >= min_usage:
        return # trimming

    if x == n-1:
        total += nxn[y][0]
        if total < min_usage:
            min_usage = total
        return # end of array

    for i in range(1, n): # x
        if visited[i] == 0:
            visited[i] = 1 # mark as visited
            dfs(i, x+1, total + nxn[y][i])
            visited[i] = 0



for test_case in range(1, int(input())+1):
    n = int(input())
    nxn = [list(map(int, input().split())) for _ in range(n)] # n x n array

    visited = [0] * n # check if visited for each row/col
    min_usage = 10000 # (max n: 10, max value: 100)

    dfs(0, 0, 0) # x,y axis each and total value


    print('#{} {}'.format(test_case, min_usage))


'''
골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91

e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89

00 18 34
48 00 55
18 07 00

이 경우 최소 소비량은 89가 된다.
'''