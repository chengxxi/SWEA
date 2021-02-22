# 2005. 파스칼의 삼각형

def pascal(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        result = [0] * n # 길이가 n인 배열 생성
        for i in range(n):
            if i == 0 or i == n-1: # 가장 처음과 마지막은 1
                result[i] = 1
            else: # 나머지는 이전 결과에서 위의 두 값 더하기
                result[i] = pascal(n-1)[i-1] + pascal(n-1)[i]
    return result
           
T = int(input())
for test_case in range(1, T + 1):
    print("#{}".format(test_case))
    num = int(input())
    for n in range(1, num+1):
        print(*pascal(n)) # 1 ~ num까지의 pascal 결과 출력


"""
크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.

2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

N이 4일 경우,
 
1
1 1
1 2 1
1 3 3 1


N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.

"""