# 1219. 길찾기

def dfs(n): # n: current node
    ans = []
    stack = [0] * 100 # node 수만큼 stack
    visited = [0] * 101 # 방문 배열
    top = -1

    top += 1
    stack[top] = n
    
    while top >= 0:
        cur = stack[top] # current
        top -= 1

        if visited[cur] == 0: # cur 안 가본 길이라면
            ans.append(cur)
            visited[cur] = 1 # 방문했다고 표시

        # 인접한 정점 탐색
        for i in range(0, 101):
            if adj[cur][i] == 1 and visited[i] == 0: # 연결되어 있는데 안 가본 길
                top += 1
                stack[top] = i
    
    return ans # DFS 경로 리스트 반환



for test_case in range(10):
    tc, r = map(int, input().split()) # test_case 번호 / 간선 수
    edge = list(map(int, input().split()))
    # for _ in range(r): # 간선 정보를 리스트 edge에 저장
    #     p1, p2 = map(int, input().split())
    #     edge.append(p1)
    #     edge.append(p2)
    
    # 인접행렬 생성
    adj = [[0 for _ in range(101)] for _ in range(101)]
    for i in range(r):
        n1, n2 = edge[i * 2], edge[i*2 + 1]
        adj[n1][n2] = 1 # 방향성 고려

    s, g = 0, 99 # 시작 노드 / 도착 노드

    anslist = dfs(s)
   
    if g in anslist: # 길이 존재한다면
        print("#{} 1".format(tc))
    else: # 길이 없다면
        print("#{} 0".format(tc))
    






"""
그림과 같이 도식화한 지도에서 A도시에서 출발하여 B도시로 가는 길이 존재하는지 조사하려고 한다.

길 중간 중간에는 최대 2개의 갈림길이 존재하고, 모든 길은 일방 통행으로 되돌아오는 것이 불가능하다.

다음과 같이 길이 주어질 때, A도시에서 B도시로 가는 길이 존재하는지 알아내는 프로그램을 작성하여라.

 - A와 B는 숫자 0과 99으로 고정된다.

 - 모든 길은 순서쌍으로 나타내어진다. 위 예시에서 2번에서 출발 할 수 있는 길의 표현은 (2, 5), (2, 9)로 나타낼 수 있다.

 - 가는 길의 개수와 상관없이 한가지 길이라도 존재한다면 길이 존재하는 것이다.

 - 단 화살표 방향을 거슬러 돌아갈 수는 없다.
"""