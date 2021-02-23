# 4866. 괄호검사 [D2]

for test_case in range(1, int(input())+1):
    brackets = input()

    def check_bracket(string):
        d = {')' : '(', '}' : '{', ']' : '['} # 괄호 쌍 딕셔너리
        stack = [] # 빈 스택 생성
        for i in range(len(string)): # 문자열 내에서 반복 수행
            if string[i] in '({[': # 열린 괄호라면
                stack.append(string[i]) # push한다
            elif string[i] in ')}]': # 닫힌 괄호라면
                if stack: # 그런데 stack이 비어있지 않으면
                    top = stack.pop() # pop한다
                    if d[string[i]] != top: # top으로 뽑아온 것이랑 string[i] 즉 괄호 쌍이 일치하지 않으면
                        return False # False를 return한다
                else: # stack이 비어있으면
                    return False
                
        return len(stack) == 0 # True / False

    ans = check_bracket(brackets)

    if ans: # True
        print("#{} 1".format(test_case))
    else: # False
        print("#{} 0".format(test_case))


"""
for test_case in range(1, int(input())+1):
    brackets = input()

    def check_bracket(string):
        stack = []
        for i in range(len(string)):
            if string[i] == "(":
                stack.append(i)
            elif string[i] == ")":
                stack.pop()
        return stack

    ans = check_bracket(brackets)
    if not ans:
        print("#{} 1".format(test_case))
    else:
        print("#{} 0".format(test_case))
"""




"""
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
 

예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 
입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
 
정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
 
print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.
"""