# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로

# 인접한 것에 대한 고민

# def check_maze(start, end):
#     stack = []
#     stack.append(maze[0][start])
#     while True:
#         r = 0; c = 0
#         # 우 / 하 / 좌 /상
#         dr = [0, 1, 0, -1]
#         dc = [1, 0, -1, 0]
#
#         if maze[r][c] == 0 and visited[r][c] != 0: # 안 가본 통로
#             stack.append(maze[r][c])


# stack 말고 DFS로 풀어보기
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def check_maze(r, c):  # start 지점의 좌표
    global result

    if maze[r][c] == 3:  # 도착 지점의 좌표이면
        result = 1
        return  # 끝냄
    elif maze[r][c] == 0:
        maze[r][c] = 9  # 방문배열 대신 9로 marking

    for k in range(4):  # 4방향 탐색
        nr = r + dr[k]
        nc = c + dc[k]

        # if nr < 0 or nr >= N or nc < 0 or nc >= N:
        #     continue # 범위 밖을 벗어난 경우 skip
        #
        # if maze[nr][nc] == 1 or maze[nr][nc] == 9:
        #     continue # 벽이거나 이미 방문했으면 skip

        if (0 <= nr < N and 0 <= nc < N and (maze[nr][nc] == 0 or maze[nr][nc] == 3)) and maze[nr][nc] != 9:
            check_maze(nr, nc)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]  # N X N
    result = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                ei, ej = i, j

    check_maze(ei, ej)

    print("#{} {}".format(test_case, result))



"""
# 0은 통로, 1은 벽, 2는 출발, 3은 도착

NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.

다음은 5x5 미로의 예이다.
13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

# result:
[[1, 3, 1, 9, 1],
 [1, 9, 1, 9, 1],
 [1, 9, 1, 9, 1],
 [1, 9, 1, 9, 1],
 [1, 9, 9, 2, 1]]
"""