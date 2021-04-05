# 1231. [S/W 문제해결 기본] 9일차 - 중위순회

def inorder(node_index):
    if node_index:
        inorder(tree[int(node_index)][1])
        print(tree[int(node_index)][0], end='')
        inorder(tree[int(node_index)][2])


for test_case in range(1, 11):
    N = int(input()) # 정점의 총 수
    tree = [[0] * 3 for _ in range(N+1)]

    # 정점 정보 받아와서 저장하기
    for n in range(1, N+1): # 각 정점 정보
        data = input().split()
        for i in range(len(data)-1):
            tree[n][i] = data[i+1]



    print('#{}'.format(test_case), end=' ')
    inorder(1) # root
    print()



    # tree[n][0] = int(data[0]) # 정점 번호
        # tree[n][1] = data[1] # 해당 정점의 알파벳
        #
        # if len(data) == 3:
        #     tree[n][2] = data[2]



        # if len(data) == 2:
        #
        # if len(data) == 3:
        #     left = int(data[2]) # 왼쪽 자식 노드
        # if len(data) == 4:
        #     left, right = int(data[2]), int(data[3]) # 왼쪽, 오른쪽 자식 노드
        #




"""
다음은 특정 단어(또는 문장)를 트리 형태로 구성한 것으로, in-order 형식으로 순회하여 각 노드를 읽으면 원래 단어를 알 수 있다고 한다.



위 트리를 in-order 형식으로 순회할 경우 SOFTWARE 라는 단어를 읽을 수 있다.

[제약 사항]

총 10개의 테스트 케이스가 주어진다.

총 노드의 개수는 100개를 넘어가지 않는다.

트리는 완전 이진 트리 형식으로 주어지며, 노드당 하나의 알파벳만 저장할 수 있다.

노드가 주어지는 순서는 아래 그림과 같은 숫자 번호대로 주어진다.
"""