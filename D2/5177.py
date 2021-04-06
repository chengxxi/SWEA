#  5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙

# 자식 노드가 부모 노드보다 큰 값을 가지도록 각자 위치 변경
def define_min_heap(node):
    while tree[node][1] < tree[node//2][1]:
        tree[node][1], tree[node//2][1] = tree[node//2][1], tree[node][1]
        # 자리 바꾼 후, 확정을 위해 바꾼 부모 노드 위치에서 재귀 호출
        define_min_heap(node//2)


for test_case in range(1, int(input())+1):
    N = int(input()) # number of nodes
    rawdata = list(map(int, input().split()))

    ### tree 구성하기
    tree = [[0] * 3 for _ in range(N+1)]

    for i in range(1, N+1):
        tree[i][1] = rawdata[i-1]
        if i * 2 <= N:
            tree[i][0] = i * 2
        if i * 2 + 1 <= N:
            tree[i][2] = i * 2 + 1

    # print(tree)

    for i in range(1, N+1):
        define_min_heap(i)
        # tree[i][1]에 순서대로 정렬된 결과

    ancestors = 0

    ### 조상 합 구하기
    while N//2 != 0:
        ancestors += tree[N//2][1]
        N //= 2

    print('#{} {}'.format(test_case, ancestors))


   #
   #
   # ancestors = []
   #
   #
   #
   #
   # print('#{} {}'.format(test_case, sum(ancestors)))



"""
이진 최소힙은 다음과 같은 특징을 가진다.

    - 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.

    - 부모 노드의 값<자식 노드의 값을 유지한다. 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.

    - 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더 이상 오른쪽이 없는 경우 다음 줄로 1씩 증가한다.

예를 들어 7, 2, 5, 3, 4, 6이 차례로 입력되면 다음과 같은 트리가 구성된다.



이때 마지막 노드인 6번의 조상은 3번과 1번 노드이다.

1000000이하인 N개의 서로 다른 자연수가 주어지면 입력 순서대로 이진 최소힙에 저장하고, 마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램을 작성하시오.
"""