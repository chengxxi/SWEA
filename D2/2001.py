# 2001: 파리 퇴치

for test_case in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)] # n X n
    # mxm = [[0] * m for _ in range(m)] # m X m (blank)

    # # m의 왼쪽 구석 좌표 기준, n-m까지 가능한
    # for k in range(m):
    #     for l in range(m):
    #         for i in range(0, n-m+1):
    #             for j in range(0, n-m+1):
    #                 mxm[k][l] = arr[i+k][j+l]

    msum = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            mxm = 0
            for k in range(i, i+m):
                for l in range(j, j+m):
                    mxm += arr[k][l]
            if mxm > msum:
                msum = mxm
    
   
    print("#{} {}".format(test_case, msum))

"""
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.

아래는 N=5 의 예이다.

M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.

죽은 파리의 개수를 구하라!

예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.

1. N 은 5 이상 15 이하이다.

2. M은 2 이상 N 이하이다.

3. 각 영역의 파리 갯수는 30 이하 이다.
"""
