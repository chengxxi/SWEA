# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임
'''
분할정복: 큰 문제를 해결할 할 수 있는 작은 문제로 분할해서 정복해 나가는 방법
(i+j)//2 | (i+j)//2+1
'''

def find(l, r): # left / right
    if l == r: # one card left
        return l

    result1 = find(l, (l+r)//2)
    result2 = find((l+r)//2+1, r)

    if card[result1] == card[result2]:
        return result1
    else:
        # 가위1, 바위2, 보3
        if card[result1] == 1 and card[result2] == 2:
            return result2
        if card[result1] == 1 and card[result2] == 3:
            return result1
        if card[result1] == 2 and card[result2] == 1:
            return result1
        if card[result1] == 2 and card[result2] == 3:
            return result2
        if card[result1] == 3 and card[result2] == 1:
            return result2
        if card[result1] == 3 and card[result2] == 2:
            return result1


T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # number of cards
    card = [0] + list(map(int, input().split())) # card info

    result = find(1, N)
    print("#{} {}".format(test_case, result))


"""
사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다. 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다. 게임 룰은 다음과 같다.


1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다. 전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.

그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데, i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다.

(i+j)//2 | (i+j)//2+1

두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식이다.

다음은 4명이 카드를 비교하는 경우로, 숫자 1은 가위, 2는 바위, 3은 보를 나타낸다. 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는 바꾸지 않는다.


N명이 학생들이 카드를 골랐을 때 1등을 찾는 프로그램을 만드시오.
"""