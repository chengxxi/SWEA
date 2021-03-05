# 1227. [S/W 문제해결 기본] 7일차 - 미로2

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs():
    q = []  # queue
    q.append((sr, sc))  # start point

    maze[sr][sc] = 1  # 이미 지나온 곳은 벽으로 만들어버림 (다시 방문하지 않기 위해)

    while q:
        n = q.pop(0)  # queue에서 좌표 하나 꺼내옴
        for k in range(4):
            nr = n[0] + dr[k]
            nc = n[1] + dc[k]

            if maze[nr][nc] == 1:
                continue
            elif maze[nr][nc] == 0:  # road not taken
                q.append((nr, nc))  # queue에 좌표를 넣음
                maze[nr][nc] = 1  # mark as visited
            elif maze[nr][nc] == 3:  # end point
                return 1

    return 0  # couldn't found the end point


for _ in range(10):
    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(100)]  # 100 X 100

    for i in range(100):
        if 2 in maze[i]:
            sr = i
            sc = maze[i].index(2)

    print("#{} {}".format(test_case, bfs()))



"""
아래 그림과 같은 미로가 있다. 100*100 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.
"""