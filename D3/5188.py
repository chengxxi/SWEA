# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합

dx = [0, 1] # right
dy = [1, 0] # down

def dfs(x, y, total):
    global minsum

    total += nxn[x][y]

    if total >= minsum:
        return # trimming

    if x == n-1 and y == n-1:
        if total < minsum:
            minsum = total
        return # end of array

    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < n and ny < n:
            dfs(nx, ny, total)


for test_case in range(1, int(input())+1):
    n = int(input())
    nxn = [list(map(int, input().split())) for _ in range(n)] # n x n array

    minsum = 1690 # 13 * 13 * 10 (max n: 13, max value: 10)

    dfs(0, 0, 0)


    print('#{} {}'.format(test_case, minsum))






'''
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.

1 2 3
2 3 4
3 4 5

그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.
'''