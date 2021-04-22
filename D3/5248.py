# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기 [D3]

def grouping(idx): # dfs
    visited[idx] = 1

    for j in range(1, n+1):
        if nxn[idx][j] == 1 and visited[j] == 0:
            grouping(j)



for test_case in range(1, int(input())+1):
    n, m = map(int, input().split())
    nxn = [[0] * (n+1) for _ in range(n+1)]
    mlist = list(map(int, input().split()))
    visited = [0] * (n+1)

    for i in range(m): # pairs
        x, y = mlist[i*2], mlist[i*2+1]
        nxn[x][y], nxn[y][x] = 1, 1

    cnt = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            grouping(i) # index
            cnt += 1


    print('#{} {}'.format(test_case, cnt))



#
# a = [1, 2]
# b = [[1, 3], [1, 2, 3], [2, 3, 4]]
# cnt = 0
# for k in a:
#     if k in b:
#         cnt += 1
#
# if cnt == len(a):
#     print('a')




'''
수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출하였다.

한 조의 인원에 제한을 두지 않았기 때문에, 한 사람이 여러 장의 종이를 제출하거나
여러 사람이 한 사람을 지목한 경우 모두 같은 조가 된다.

예를 들어 1번-2번, 1번-3번이 같은 조가 되고 싶다고 하면, 1-2-3번이 같은 조가 된다.
 번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.

1번부터 N번까지의 출석번호가 있고, M 장의 신청서가 제출되었을 때 전체 몇 개의 조가 만들어지는지 출력하는 프로그램을 만드시오.
'''