# 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth

# 후위표기법의 stack을 이용한 계산

operator = ["*", "/", "+", "-"]
end = "."

def is_number(x):
    if x not in operator and x != end:
        return True
    else:
        return False

T = int(input())
for test_case in range(1, T+1):
    forthinput = list(map(str, input().split()))
    stack = []
    answer = "error" # default
    stack.append(forthinput[0])

    for token in forthinput[1:]:
        if len(stack) == 0:
            break
        if is_number(token): # 숫자라면
            stack.append(token) # push한다
        elif token in operator: # 연산자라면
            # 두 수를 뽑아 연산한다
            if len(stack) > 1:
                token1 = int(stack.pop())
                token2 = int(stack.pop())

                if token == "+":
                    stack.append(token2 + token1)
                elif token == "-":
                    stack.append(token2 - token1)
                elif token == "*":
                    stack.append(token2 * token1)
                elif token == "/":
                    stack.append(token2 / token1)
            else: break # 두 수를 뽑지 못하면 error
        if token == end:
            if len(stack) == 1: # 이 조건 주의
	            answer = int(stack.pop()) # int에 유의

    print("#{} {}".format(test_case, answer))



"""
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.


3 4 + .


Forth에서는 동작은 다음과 같다.


숫자는 스택에 넣는다.

연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.

‘.’은 스택에서 숫자를 꺼내 출력한다.



Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
"""



"""
# 오답 해결 과정

1) 끝이 아닌데 stack의 길이가 0이면 더이상 연산하지 않고 error
2) 두 수를 뽑지 못하는 경우 (stack의 길이가 0, 1) error
3) 마지막 수 하나가 남아 있을 대, 그것이 정답이 되어야 한다
4) 나눗셈에서 FLOAT가 될 수 있으니 INT 형변환


7
4 3 - .
4 2 / .
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
3 4 + 5 6 * + 7 +  .
3 3 - 4 .
"""