# 4869. 종이붙이기 [D2]

def paper(point): # point : 탐색할 위치
    if point == N: # 범위의 끝에 도달하면 (같으면)
        return 1
    if point > N: # 범위 밖에 있으면
        return 0
    return paper(point+10) + paper(point+20) * 2

for test_case in range(1, int(input())+1):
    N = int(input())
    cases = paper(0)

    print("#{} {}".format(test_case, cases))


"""
어린이 알고리즘 교실의 선생님은 경우의 수 놀이를 위해, 그림처럼 가로x세로 길이가 10x20, 20x20인 직사각형 종이를 잔뜩 준비했다.

그리고 교실 바닥에 20xN 크기의 직사각형을 테이프로 표시하고, 이 안에 준비한 종이를 빈틈없이 붙이는 방법을 찾아보려고 한다.
N이 30인 경우 다음 그림처럼 종이를 붙일 수 있다.

10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산하는 프로그램을 만드시오. 
직사각형 종이가 모자라는 경우는 없다.
"""