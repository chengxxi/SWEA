# 1210: Ladder

def target(arr):
    for idx in range(len(arr)):
        if arr[99][idx] == 2:
            return idx

def ladder(arr, target):
    # starts from 2
    row = 99 # Nth row (default: last line)
    column = target # arr[row].index(2) # 마지막 줄에서 2 값을 가진 곳의 index

    dir = 'up' # set direction (up / left / right)
    while row > 0:
        if dir == 'up': # while going up...
            if 0 <= column - 1 < 100 and arr[row][column-1] == 1:
                column -= 1 # move to left
                dir = 'left' # upperleft is 1
            elif 0 <= column + 1 < 100 and arr[row][column+1] == 1:
                column += 1 # move to right
                dir = 'right' # upperright is 1
            else: # keep going
                row -= 1 # go up without changing direction
        elif dir == 'left':
            if arr[row-1][column] == 1: # upper line is 1
                row -= 1 # go up
                dir = 'up' # change direction
            else:
                column -= 1 # move left
        else: # 'right' dir ?
            if arr[row-1][column] == 1:
                row -= 1 # go up
                dir = 'up' # change direction
            else:
                column += 1 # move right
    
    return column

for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)] # 100X100

    idx = target(arr)
    answer = ladder(arr, idx)
    
    print("#{} {}".format(test_case, answer))


"""
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.

김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.

사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고(이 예에서는 2개가 추가됨) 이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.

X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.

방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

문제의 X표시에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.



https://velog.io/@jinho0705/SWEA-1210.-Ladder1
"""