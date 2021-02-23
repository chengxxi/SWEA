# 4871. 그래프 경로 [D2]
def dfs(n): # n : current node
    ans = []
    stack = [0] * v # node 수만큼 stack
    visited = [0] * (v+1) # 방문 배열
    top = -1

    top += 1
    stack[top] = n
    
    while top >= 0:
        cur = stack[top]
        top -= 1

        if visited[cur] == 0:
            ans.append(cur)
            visited[cur] = 1

        # 인접한 정점 탐색
        for i in range(1,v+1):
            if adj[cur][i] == 1 and visited[i] == 0:
                top += 1
                stack[top] = i
    
    return ans # DFS 경로 리스트 반환

for test_case in range(1, int(input())+1):
    v, e = map(int, input().split()) # 노드 수 / 간선 수
    edge = list()
    for _ in range(e): # 간선 정보를 edge에 정리
        p1, p2 = map(int, input().split())
        edge.append(p1)
        edge.append(p2)
    # 인접행렬 생성
    adj = [[0 for _ in range(v+1)] for _ in range(v+1)]
    for i in range(e):
        n1, n2 = edge[i*2], edge[i*2+1]
        adj[n1][n2] = 1
        # adj[n2][n1] = 1 # 방향성
    
    s, g = map(int, input().split()) # 출발 노드 / 도착 노드
    
    anslist = dfs(s)
   
    
    if g in anslist:
        print("#{} 1".format(test_case))
    else:
        print("#{} 0".format(test_case))


"""
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.

두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
 
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.

노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
"""


"""
input
3
---
6 5 (v, e)

1 4
1 3
2 3
2 5
4 6

1 6 (s, g)
---
7 4 (v, e)

1 6
2 3
2 6
3 5

2 5 (s, g)
---
9 9 (v, e)

2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8

1 9 (s, g)
---
"""
