# 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree [D2]


def inorder(node_index):
    global cnt
    if node_index:
        cnt += 1
        inorder(tree[node_index][0])
        inorder(tree[node_index][2])



for test_case in range(1, int(input())+1):
    E, N = map(int,input().split()) # 간선의 개수
    tree = [[0] * 3 for _ in range(E+2)] # tree

    # E개의 부모 - 자식 노드 번호 쌍
    rawdata = list(map(int, input().split()))
    parent = 0

    for idx, number in enumerate(rawdata):
        if idx % 2: # child node
            child = number
            if not tree[parent][0]: # left가 비어있으면s
                tree[parent][0] = child
            else:
                tree[parent][2] = child # right

        else:
            parent = number # parent node


    cnt = 0
    inorder(N)
    print('#{} {}'. format(test_case, cnt))




"""
트리의 일부를 서브 트리라고 한다. 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.



주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없고, 부모가 없는 노드가 전체의 루트 노드가 된다.

이런 경우의 트리는 부모 노드를 인덱스로 다음과 같은 방법으로 나타낼 수 있다. 자식 노드가 0인 경우는 노드가 자식이 없는 경우이다.
"""