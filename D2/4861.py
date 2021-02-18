# 4861: 회문 

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N X N, M: len(pal) 
    arr = [list(input()) for _ in range(N)] 
    answer = ''

    # row
    pal = 0
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[i][j+k] == arr[i][j+M-1-k]:
                    pal += 1
            if pal == M // 2:
                for l in range(j, j+M):
                    answer += arr[i][l]
            pal = 0

    # col
    pal = 0
    for j in range(N):
        for i in range(N-M+1):
            for k in range(M//2):
                if arr[i+k][j] == arr[i+M-1-k][j]:
                    pal += 1
            if pal == M // 2:
                for l in range(i, i+M):
                    answer += arr[l][j]
            pal = 0

    print("#{} {}".format(test_case, answer))


"""
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. 
NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다. 

예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.
"""
