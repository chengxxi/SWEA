# 4873. 반복문자 지우기 [D2]

def remove_repeated_char(string):
    stack = [] # stack 생성
    # top = '' # 가장 마지막에 삽입된 자료 // 의 위치, -1 : empty stack

    for i in range(len(string)):
        # stack이 비었거나, 스택의 마지막 값이 데이터의 값과 다를 때
        if not stack or stack[-1] != string[i]:
            stack.append(string[i])
        # stack에 값이 있고, 그 값이 데이터의 값과 같을 때
        elif stack and stack[-1] == string[i]:
            if stack != []:
                stack.pop()
    return stack


for test_case in range(1, int(input())+1):
    print("#{}".format(test_case), end=" ")
    string = input()

    ans = remove_repeated_char(string)
    # print(*ans)
    print(len(ans)) 


"""
문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.

반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
 

다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.
 

CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.

CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.

CAA 연속 문자 AA를 지운다.

C 1글자가 남았으므로 1을 리턴한다.
"""
