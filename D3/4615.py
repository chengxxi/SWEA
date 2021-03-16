# 4615. 재미있는 오셀로 게임

for test_case in range(1, int(input())+1):
    n, m = map(int, input().split()) # arr size, 돌 놓는 횟수
    board = [[0] * n for _ in range(n)]
    delta = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)] # 8방향

    mid = n // 2 # 정중앙에 초기 돌 세팅
    board[mid][mid] = 2
    board[mid-1][mid] = 1
    board[mid][mid-1] = 1
    board[mid-1][mid-1] = 2

    for _ in range(m):
        # 행렬 좌표 값이 설명과 반대라고 한다
        y, x, s = map(int, input().split())
        x -= 1; y -= 1 # index로 사용하기 위해

        if not board[x][y]:
            board[x][y] = s
            for i in range(8):
                dx, dy = delta[i]
                nx, ny = x + dx, y + dy
                reverse = [] # 뒤집을 좌표 저장

                while True:
                    # 범위 밖
                    if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                        reverse = []
                        break
                    # 공백인지 확인
                    if board[nx][ny] == 0:
                        reverse = []
                        break
                    # 같은 색깔을 만났다면 멈춤
                    if board[nx][ny] == s:
                        break
                    else: # 다른 색이라면 저장
                        reverse.append((nx, ny))

                    nx += dx
                    ny += dy
                # 색을 뒤집어준다
                for rx, ry in reverse:
                    board[rx][ry] = s

    # 각 돌의 수 세기
    white = 0; black = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: white += 1
            elif board[i][j] == 2: black += 1
    #black = n ** 2 - white

    print("#{} {} {}".format(test_case, white, black))


"""
오셀로라는 게임은 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.

보드는 4x4, 6x6, 8x8(가로, 세로 길이) 크기를 사용한다. 6x6 보드에서 게임을 할 때, 처음에 플레이어는 다음과 같이 돌을 놓고 시작한다(B : 흑돌, W : 백돌).

4x4, 8x8 보드에서도 동일하게 정가운데에 아래와 같이 배치하고 시작한다.


그리고 흑, 백이 번갈아가며 돌을 놓는다.

처음엔 흑부터 시작하는데 이 때 흑이 돌을 놓을 수 있는 곳은 다음과 같이 4군데이다.


플레이어는 빈공간에 돌을 놓을 수 있다.

단, 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고, 그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.

(여기에서 "사이"란 가로/세로/대각선을 의미한다.)

(2, 3) 위치에 흑돌을 놓은 후의 보드는 다음과 같다.


이런 식으로 번갈아가며 흑, 백 플레이어가 돌을 놓는다.

만약 돌을 놓을 곳이 없다면 상대편 플레이어가 다시 돌을 놓는다.

보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고 그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.
"""