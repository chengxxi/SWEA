# 2805. 농작물 수확하기
'''
가운데축: N//2 (열 전체)
그 외: 아래위로 한 칸씩 빠짐
'''


for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)] # N X N

    total = 0; middle = N // 2
    for i in range(N):
        for j in range(N):
            if abs(middle-i) + abs(middle-j) <= middle:
                total += arr[i][j]

    print("#{} {}".format(test_case, total))



"""
N X N크기의 농장이 있다.

이 농장에는 이상한 규칙이 있다.

규칙은 다음과 같다.


   ① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)

   ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.


1 X 1크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 3이다.

3 X 3크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 16 (3 + 2 + 5 + 4 + 2)이다.

5 X 5크기의 농장에서 자라는 농작물의 수확하여 얻을 수 있는 수익은 25 (3 + 2 + 1 + 1 + 2 + 5 + 1 + 1 + 3 + 3 + 2 + 1)이다.

농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.
"""