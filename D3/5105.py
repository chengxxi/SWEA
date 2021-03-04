# why not working...
# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
# cf. 4875번


# 범위 안에 있는지
def is_safe(y, x):
    return 0 <= y < N and 0 <= x < N and (maze[y][x] == 0 or maze[y][x] == 3)

def bfs(r, c): # start 지점의 좌표
    global result
    q.append((r, c)) # 좌표를 queue에 넣는다
    visited.append((r, c)) # 방문배열에도 좌표를 넣는다

    while q: # queue에 값이 남아 있을 때
        r, c = q.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if is_safe(nr, nc) and (nr, nc) not in visited:
                # 범위 안에 있고, 방문하지 않았다면
                q.append((nr, nc)) # 좌표를 queue에 넣고
                visited.append((nr, nc)) # 방문 표시
                distance[nr][nc] = distance[r][c] + 1

                if maze[nr][nc] == 3:
                    result = distance[nr][nc] - 1
                    return


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]  # N X N
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j

    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    result = 0
    q = []
    distance = [[0] * N for _ in range(N)]
    bfs(r, c)

    print("#{} {}".format(test_case, result))



"""                                                                               
NxN 크기의 미로에서 출발지 목적지가 주어진다.                                                       

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.                          

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.                      

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.                              

13101                                                                             
10101                                                                             
10101                                                                             
10101                                                                             
10021                                                                             

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.                       
"""