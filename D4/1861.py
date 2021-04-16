# 1861. 정사각형 방

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(x, y, st, cnt):
    global start, rooms

    if cnt > rooms:
        rooms = cnt
        start = st
    elif cnt == rooms and st < start:
        start = st


    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if nxn[nx][ny] == nxn[x][y] + 1:
                dfs(nx, ny, st, cnt+1)



for test_case in range(1, int(input())+1):
    n = int(input())
    nxn = [list(map(int, input().split())) for _ in range(n)] # n x n array

    start = 0
    rooms = 0

    for i in range(n):
        for j in range(n):
            dfs(i, j, nxn[i][j], 1)


    print('#{} {} {}'.format(test_case, start, rooms))

    

'''
N**2개의 방이 N×N형태로 늘어서 있다.

위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.

당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.

물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.

처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.
'''
