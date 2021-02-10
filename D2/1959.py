# 1959: 두 개의 숫자열

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    aj = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    
    #longer = len(aj) if len(aj) > len(bj) else len(bj) # 길이가 더 긴 리스트를 기준으로
    # abs(len(aj) - len(bj)) # 길이의 차이

    answer = 0
    for i in range(abs(N-M)+1):
        if N > M:
            multipled = 0
            for j in range(M):
                multipled += aj[i+j] * bj[j]
            if answer < multipled:
                answer = multipled 
        if N < M:
            multipled = 0
            for k in range(N):
                multipled += aj[k] * bj[i+k]
            if answer < multipled:
                answer = multipled





        # # 1 cycle
        # result = []
        # for i in range(gap):
        #     add_all += aj[i] * bj[i]
        # result.append(add_all)

          
    print("#{} {}".format(test_case, answer))
              

  

"""
N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.

아래는 N =3 인 Ai 와 M = 5 인 Bj 의 예이다.

Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.

단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.

서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.
"""