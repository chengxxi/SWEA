# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색 [D2]


# def inorder(node_index):
#     global cnt
#     if node_index:
#         cnt += 1
#         inorder(tree[node_index][0])
#         inorder(tree[node_index][2])


def treebuilding(node):
    global cnt
    if node <= N: # size of arr
        treebuilding(node * 2) # 왼쪽은 현재 노드 index * 2
        tree[node] = cnt
        cnt += 1
        treebuilding(node * 2 + 1) # 오른쪽은 현재 노드 index * 2



for test_case in range(1, int(input())+1):
    N = int(input()) # size of arr

    tree = [0 for _ in range(N+1)]
    cnt = 1
    treebuilding(1)


    # test_case, root, N/2
    print('#{} {} {}'. format(test_case, tree[1], tree[N//2]))
    # print(tree)




"""
1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.

이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.

추가나 삭제가 없는 경우에는, 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리를 만들수 있다.

다음은 1부터 6까지의 숫자를 완전 이진 트리 형태인 이진 탐색 트리에 저장한 경우이다.



 
완전 이진 트리의 노드 번호는 루트를 1번으로 하고 아래로 내려가면서 왼쪽에서 오른쪽 순으로 증가한다.

N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과, N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.
"""