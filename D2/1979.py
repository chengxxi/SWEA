# 1979. 어디에 단어가 들어갈 수 있을까

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) # N : sq, K : word length
    
    arr = [list(map(int, input().split())) for _ in range(N)] # word puzzle
    # 1을 만나면 cnt += 1, 0 만나면 초기화; cnt == K 인 경우 수 찾아서 result에 더한다
    result = 0

    # row
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1
            
    # col
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1
    
        
    print("#{} {}".format(test_case, result))



"""
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.
"""