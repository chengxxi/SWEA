# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임

'''
run: 연속된 숫자가 3개 이상
triplet: 같은 숫자가 3개 이상
'''

def is_babygin(player):
    for i in range(10):
        if player[i] == 3:
            return True # triplet
        if player[i] >= 1 and player[i+1] >= 1 and player[i+2] >= 1:
            return True # run
    return False

for test_case in range(1, int(input())+1):
    deck = list(map(int, input().split()))

    player1 = [0] * 12 # 0 ~ 9 + index
    player2 = [0] * 12 # 0 ~ 9 + index

    result = 0
    # # dividing cards
    # for card in range(12):
    #     if card % 2 == 0:
    #         player1[deck[card]] += 1
    #     else:
    #         player2[deck[card]] += 1

    card = 0
    while card < 12:
        if card % 2 == 0:
            player1[deck[card]] += 1
            card += 1

            if is_babygin(player1):
                result = 1
                break
        else:
            player2[deck[card]] += 1
            card += 1

            if is_babygin(player2):
                result = 2
                break


    print('#{} {}'.format(test_case, result))



'''
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때,
연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.

게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며,
6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.

두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오.
만약 무승부인 경우 0을 출력한다.

예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를,
플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.

이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.
'''