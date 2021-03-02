# 1224. [S/W 문제해결 기본] 6일차 - 계산기3

def is_number(x):  # 피연산자인지 확인
    if x not in operator and x not in bracket:
        return True
    else:
        return False


def isp(token):  # isp: 스택의 top 연산자 우선순위 (in-stack priority)
    if token == "*":
        return 2
    elif token == "+":
        return 1
    elif token == "(":
        return 0


def icp(token):  # icp: 스택으로 들어갈 연산자의 우선순위 (in-coming priority)
    if token == "*":
        return 2
    elif token == "+":
        return 1
    elif token == "(":
        return 3


for test_case in range(1, 11):
    length = int(input())
    infix = list(input())  # 입력을 리스트화
    postfix = []  # 출력 결과 저장
    stack = []
    operator = ["*", "+"]
    bracket = ["(", ")"]


    for token in infix:
        if is_number(token): # True: 숫자인 경우
            postfix.append(token)
        elif token == ")": # 닫는 괄호면
            while len(stack) > 0:  # stack에 값이 있는 동안
                top = stack.pop()  # 값을 꺼낸다
                if top == '(':  # 여는 괄호가 나올 때까지
                    break
                postfix.append(top)
        else: # 연산자
            if len(stack) == 0:
                stack.append(token)
            else:
                while len(stack) > 0: # stack에 값이 있을 동안
                    top = stack[-1] # 가장 마지막 값
                    if isp(top) < icp(token): # stack 안의 연산자가 top보다 우선순위가 높으면,
                        break
                    postfix.append(stack.pop()) # stack에서 pop해서 출력 결과에 담기
                stack.append(token) # 토큰의 연산자를 stack에 push


    while len(stack) > 0:  # stack에 뭐가 남아있다면
        remain = stack.pop()  # pop하고
        postfix.append(remain)  # 출력


    s = []  # empty stack
    for token in postfix:  # 수식의 요소별로 다음을 수행
        if is_number(token):  # 피연산자
            s.append(token)  # push
        else:  # 연산자
            token1 = int(s.pop())
            token2 = int(s.pop())
            if token == "*":
                s.append(token2 * token1)
            elif token == "+":
                s.append(token2 + token1)

    final_ans = s.pop()
    print("#{} {}".format(test_case, final_ans))



"""
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+(4+5)*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"345+6*+7+"

변환된 식을 계산하면 64를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 문자열 중간에 괄호가 들어갈 수 있다.

이 때 괄호의 유효성 여부는 항상 옳은 경우만 주어진다.

피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

"""