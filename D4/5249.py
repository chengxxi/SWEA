# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리 [D4]

def make_set(x):
    parents[x] = x # itself
    rank[x] = 0


def find_set(x):
    if x != parents[x]: # x is not root
        parents[x] = find_set(parents[x]) # path compression
    return parents[x]


def link(x, y):
    if rank[x] > rank[y]:
        parents[y] = x
    else:
        parents[x] = y

    if rank[x] == rank[y]:
        rank[y] += 1


def union(x, y):
    link(find_set(x), find_set(y))


def kruskal(g): # graph
    mst = [] # disjoint sets

    for i in range(v):
        make_set(i)

    g.sort(key = lambda t: t[2])
    mst_cost = 0 # weight of mst

    while len(mst) < v:
        u, vv, val = g.pop(0) # least weight
        if find_set(u) != find_set(vv):
            union(u, vv)
            mst.append((u, vv))
            mst_cost += val

    return mst_cost




for test_case in range(1, int(input())+1):
    v, e = map(int, input().split())
    adj = [list(map(int, input().split())) for _ in range(e)] # nodes and weight
    # sorted by weight
    adj = sorted(adj, key = lambda x: x[2])

    parents = [i for i in range(v+1)]
    rank = [i for i in range(v+1)]

    answer = kruskal(adj)


    print('#{} {}'.format(test_case, answer))


'''
그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 
가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.

0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때, 
이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.
'''

