# 1223. 계산기2

for test_case in range(1, 11):
    length = int(input())
    inf = input()  # 입력된 수식
    infix = list(inf)  # 입력을 리스트로 바꿈
    postfix = []  # 출력 결과 저장
    stack = []
    operator = ["*", "/", "+", "-"]
    bracket = ["(", ")"]


    def is_number(x):  # 피연산자인지 확인
        if x not in operator and x not in bracket:
            return True
        else:
            return False


    def isp(token):  # isp: 스택의 top 연산자 우선순위 (in-stack priority)
        if token == "*" or token == "/":
            return 2
        elif token == "+" or token == "-":
            return 1
        elif token == "(":
            return 0


    def icp(token):  # icp: 스택으로 들어갈 연산자의 우선순위 (in-coming priority)
        if token == "*" or token == "/":
            return 2
        elif token == "+" or token == "-":
            return 1
        elif token == "(":
            return 3


    def InfixToPostfix(sthinput):  # sthinput: 수식
        for token in sthinput:  # x의 각 token들에 대해서,
            if is_number(token) == True:  # 피연산자(숫자)인 경우
                postfix.append(token)  # 출력 결과에 바로 담는다

            elif token in operator:  # 연산자인 경우
                ptkn = icp(token)  # 연산자의 우선순위를 파악한 후,

                # 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 pop
                while len(stack) > 0:  # stack이 비어있지 않을 때
                    top = stack[-1]
                    if isp(top) <= ptkn:  # stack 안의 연산자가 top보다 우선순위가 높으면,
                        break  # 바로 line60 (push to stack)
                    # 우선순위가 top 연산자의 우선순위보다 높으면,
                    postfix.append(stack.pop())  # stack에서 pop해서 출력 결과에 담기
                stack.append(token)  # 토큰의 연산자를 stack에 push

            elif token in bracket:  # 괄호라면
                if token == "(":
                    stack.append(token)  # stack에 "(" push
                if token == ")":
                    while True:
                        x = stack.pop  # 왼쪽 괄호가 나올 때까지 계속 pop
                        if x == "(":
                            break  # pop은 하고 출력은 하지 않는다

        while len(stack) > 0:  # stack에 뭐가 남아있다면
            remain = stack.pop()  # pop하고
            postfix.append(remain)  # 출력

        return postfix  # 출력 결과 RETURN


    result = InfixToPostfix(infix)
    ans = ''
    for r in result:
        ans += r  # 결과적으로 생성된 수식
    # print(ans)

    s = []  # empty stack
    for token in ans:  # 수식의 요소별로 다음을 수행
        if is_number(token):  # 피연산자
            s.append(token)  # push
        else:  # 연산자
            token1 = int(s.pop())
            token2 = int(s.pop())
            if token == "*":
                s.append(token2 * token1)
            elif token == "/":
                s.append(token2 / token1)
            elif token == "+":
                s.append(token2 + token1)
            elif c == "-":
                s.append(token2 - token1)

    final_ans = s.pop()
    print("#{} {}".format(test_case, final_ans))
    print(inf)


"""
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+4+5*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"34+56*+7+"

변환된 식을 계산하면 44를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.
"""