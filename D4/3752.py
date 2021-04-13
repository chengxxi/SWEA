# 3752. 가능한 시험 점수

for test_case in range(1, int(input())+1):
    N = int(input()) # number of problem set
    scores = list(map(int, input().split()))

    potentialset = [0]
    visited = [0] * 10001

    for i in range(N):
        temp = []
        for p in potentialset:
            # t: new score created / p: a potential score set
            t = scores[i] + p
            if visited[t] == 0: # if not visited
                temp.append(t) # add to temporal list
                visited[t] = 1 # mark as visited

        potentialset += temp
        
        
    print('#{} {}'.format(test_case, len(potentialset)))





    # # 제한시간 초과
    # answer = []
    # for i in range(1 << N):
    #     anslist = []
    #     for j in range(N):
    #         if i & (1 << j):
    #             anslist.append(scores[j])
    #
    #     answer.append(sum(anslist))
    #
    # print('#{} {}'.format(test_case, len(set(answer))))



'''
영준이는 학생들의 시험을 위해 N개의 문제를 만들었다.

각 문제의 배점은 문제마다 다를 수 있고, 틀리면 0점 맞으면 배점만큼의 점수를 받게 된다.

학생들이 받을 수 있는 점수로 가능한 경우의 수는 몇 가지가 있을까?

예를 들어, 첫 번쨰 Testcase의 경우, 총 문제의 개수는 3개이며 각각의 배점은 2, 3, 5점이다

가능한 시험 점수의 경우의 수를 살펴보면 0, 2, 3, 5, 7, 8, 10의 7가지가 있다.

두 번째 Testcase의 경우, 총 문제의 개수는 10개이며 각각의 배점은 모두 1점이다.

가능한 시험점수의 경우의 수를 살펴보면 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10으로 모두 11가지이다.

'''