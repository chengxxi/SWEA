# 1865. 동철이의 일 분배 [D4]

# def max_efficiency(combi, row, n):
#     efficiency = 1
#
#     if n == row:
#         return combi[row]
#
#     for col in range(n):
#         combi[row] = col
#         for i in range(row):
#             if combi[i] == combi[row]:
#                 break
#             if abs(combi[i] - combi[row]) == row - i:
#                 break
#         else:
#             efficiency *= max_efficiency(combi, row+1, n)
#
#     return efficiency

def hr(idx, ef): # Human Resource: index & efficiency
    global max_efficiency
    if idx == n: # end of array
        if max_efficiency < ef:
            max_efficiency = ef
        return

    if max_efficiency >= ef:
        return


    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1 # mark as visited
            hr(idx+1, ef * (nxn[idx][i] / 100))
            visited[i] = 0




for test_case in range(1, int(input())+1):
    n = int(input())
    nxn = [list(map(int, input().split())) for _ in range(n)]

    visited = [0] * n
    max_efficiency = 0 # default

    hr(0, 1)



    print('#{} {:.6f}'.format(test_case, max_efficiency * 100))




'''
동철이가 차린 전자회사에는 N명의 직원이 있다.

그런데 어느 날 해야할 일이 N개가 생겼다.

동철이는 직원들에게 공평하게 일을 하나씩 배분하려고 한다.

직원들의 번호가 1부터 N까지 매겨져 있고, 해야 할 일에도 번호가 1부터 N까지 매겨져 있을 때, i번 직원이 j번 일을 하면 성공할 확률이 Pi, j이다.

여기서 우리는 동철이가 모든 일이 잘 풀리도록 도와주어야 한다.

직원들에게 해야 할 일을 하나씩 배분하는 방법은 여러 가지다.

우리는 여러 방법 중에서 생길 수 있는 “주어진 일이 모두 성공할 확률”의 최댓값을 구하는 프로그램을 작성해야 한다.
'''