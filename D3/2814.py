# 2814. 최장 경로 [D3]

def max_length(idx, cnt): # dfs
    global length

    visited[idx] = 1

    if length < cnt:
        length = cnt

    for j in range(1, n+1):
        if adj[idx][j] == 1 and visited[j] == 0:
            max_length(j, cnt+1)

    visited[idx] = 0



for test_case in range(1, int(input())+1):
    n, m = map(int, input().split()) # m = n - 1
    adj = [[0] * (n+1) for _ in range(n+1)] # n+1 x n+1
    visited = [0] * (n+1)

    # make adjacent array
    for _ in range(m): # edge
        x, y = map(int, input().split())
        adj[x][y], adj[y][x] = 1, 1 # no direction

    length = 0
    for i in range(1, n+1):
        max_length(i, 1)




    print('#{} {}'.format(test_case, length))


'''
N개의 정점과 M개의 간선으로 구성된 가중치가 없는 무방향 그래프에서의 최장 경로의 길이를 계산하자.

정점의 번호는 1번부터 N번까지 순서대로 부여되어 있다.

경로에는 같은 정점의 번호가 2번 이상 등장할 수 없으며, 경로 상의 인접한 점들 사이에는 반드시 두 정점을 연결하는 간선이 존재해야 한다.

경로의 길이는 경로 상에 등장하는 정점의 개수를 나타낸다.
'''