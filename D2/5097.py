# 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전
'''
다양한 solution 고민
최대한 많은 방법으로 풀어보기
'''

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    # N: 수열의 길이 / M: 연산 횟수
    nli = list(map(int, input().split()))


    ### 1. LIST ###
    for _ in range(M):
        f = nli.pop(0) # 가장 앞의 값을 뽑아서
        nli.append(f) # 맨 뒤로 붙인다

    print("#{} {}".format(test_case, nli[0]))


    ### 2. list INDEX ###
    t = M % N # M // N 만큼은 제자리로 돌아오므로, 나머지만큼 연산
    for _ in range(t):
        f = nli.pop(0)
        nli.append(f)

    print("#{} {}".format(test_case, nli[0]))


    ### 3. INDEX ###
    t = M % N
    # 결국 나머지만큼 index가 밀린 값이 처음에 오게 되므로
    print("#{} {}".format(test_case, nli[0+t]))


    ### 4. While ###
    cnt = 0

    while cnt != M:
        nli.append(nli.pop(0))
        # cnt가 M이 될 때까지, 배열의 가장 처음 값을 뽑아 뒤에 붙임
        cnt += 1

    print("#{} {}".format(test_case, nli[0]))


    ### 5. QUEUE ###
    q = []
    for n in range(N):
        q.append(nli[n])
        # queue에 nli의 값들을 넣어놓고,
    for m in range(M):
        first = q.pop(0)
        q.append(first)

    print("#{} {}".format(test_case, q[0]))


"""
N개의 숫자로 이루어진 수열이 주어진다. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.
"""