#  5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합

for test_case in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    # N: node, M: leaf node, L: target node number
    tree = [0 for _ in range(N+1)] # default tree setting

    for _ in range(M): # leaf node num & value
        leafnode, value = map(int, input().split())
        tree[leafnode] = value


    for i in range(N, 0, -1): # parent nodes
        if tree[i] == 0:
            if i*2 + 1 <= N:
                tree[i] = tree[i*2] + tree[i*2 + 1]
            else:
                tree[i] = tree[i*2]


    # print(tree)
    print('#{} {}'.format(test_case, tree[L]))




"""
완전 이진 트리의 리프 노드에 1000이하의 자연수가 저장되어 있고, 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다고 한다.

다음은 리프 노드에 저장된 1, 2, 3이 주어졌을 때, 나머지 노드에 자식 노드의 합을 저장한 예이다.


리프 노드 저장 값	자식 노드의 합을 저장한 상태

N개의 노드를 갖는 완전 이진 트리의 노드 번호는 루트가 1번이 되며, 같은 단계에서는 왼쪽에서 오른쪽으로 증가, 단계가 꽉 차면 다음단계의 왼쪽부터 시작된다.

완전 이진 트리의 특성상 1번부터 N번까지 빠지는 노드 번호는 없다.

리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 다음, 지정한 노드 번호에 저장된 값을 출력하는 프로그램을 작성 하시오.
"""