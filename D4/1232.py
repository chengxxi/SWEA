# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산

# def postorder(node):
#     if node not in ['+', '-', '*', '/']:  # number
#         return tree[node][1]
#
#     if node in ['+', '-', '*', '/']: # operand
#         left = postorder(int(tree[node][0]))
#         right = postorder(int(tree[node][2]))
#
#         if node == '+': return left + right
#         elif node == '-': return left - right
#         elif node == '*': return left * right
#         elif node == '/': return left // right



for test_case in range(1, 11):
    N = int(input()) # number of nodes
    tree = [[0] * 3 for _ in range(N+1)]
    for _ in range(N):
        data = list(map(str, input().split()))
        if len(data) == 2: # no child
            # data[0]: number of node, data[1]: value
            tree[int(data[0])][1] = int(data[1])
        elif len(data) == 4: # has 2 children
            tree[int(data[0])][1] = data[1]
            tree[int(data[0])][0] = int(data[2]) # left child
            tree[int(data[0])][2] = int(data[3]) # right child

    # print(tree)

    for node in tree[::-1]:
        left = tree[node[0]][1]
        right = tree[node[2]][1]
        # if tree[node][1] in ['+', '-', '*', '/']: # operand
        if node[1] == '+':
            node[1] = left + right
        elif node[1] == '-':
            node[1] = left - right
        elif node[1] == '*':
            node[1] = left * right
        elif node[1] == '/':
            node[1] = left // right

    # print(tree)


    print('#{} {}'.format(test_case, tree[1][1]))




"""
사칙연산으로 구성되어 있는 식은 이진 트리로 표현할 수 있다. 아래는 식 “(9/(6-4))*3”을 이진 트리로 표현한 것이다.

임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 서브 트리의 결과와 오른쪽 서브 트리의 결과를 사용해서 해당 연산자를 적용한다.



사칙연산 “+, -, *, /”와 양의 정수로만 구성된 임의의 이진트리가 주어질 때, 이를 계산한 결과를 출력하는 프로그램을 작성하라.

단, 중간 과정에서의 연산은 실수 연산으로 하되, 최종 결과값이 정수로 떨어지지 않으면 정수부만 출력한다.

위의 예에서는 최종 결과값이 13.5이므로 13을 출력하면 된다.
"""