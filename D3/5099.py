# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    # N: 화덕의 크기 (한번에 구울 수 있는 양) / M: 피자의 수
    cheese = list(map(int, input().split())) # 각 피자에 올라간 치즈의 양
    pizza = [i for i in range(M)] # 피자 번호 넘버링 / +1 해야함

    q = pizza[0:N] # 1번쨰: 앞에서부터 N개의 피자를 넣고 시작

    while len(q) > 1: # 마지막 하나가 남을 때까지
        if cheese[q[0]] >= 1: # 아직 다 안 녹은 경우
            cheese[q[0]] //= 2 # 2로 나눈 몫으로 바뀌고
            q.append(q.pop(0)) # 1번을 빼서 가장 마지막으로 (한 칸 돌린다는 뜻)
        else: # cheese[q[0]] == 0 (다 녹은 경우)
            q.pop(0)
            if N != M: # M개가 다 안 들어간 경우
                q.append(pizza[N]) # N번째 새로운 피자를 넣고
                N += 1  # 그 다음번에 들어갈 것은 N+1번 피자


    # q에는 마지막 하나가 남아 있음
    last = q.pop() + 1 # index이기 때문에 1 더해줘야

    print("#{} {}".format(test_case, last))





"""
N개의 피자를 동시에 구울 수 있는 화덕이 있다. 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.

1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.

주어진 조건에 따라 피자를 구울 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.


- 피자는 1번위치에서 넣거나 뺄 수 있다.
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.
"""