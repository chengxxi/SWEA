# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기

# def isEmpty():
#     return f == r # True / False
#
# def isFull():
#     return r == len(q) - 1 # True / False
#
# def enQueue(item):
#     global r # rear
#     if isFull(): print("Queue is Full")
#     else:
#         r += 1 # rear를 뒤로 한 칸 옮기고
#         q[r] = item
#
# def deQueue():
#     global f # front
#     if isEmpty(): print("Queue is Empty")
#     else:
#         f += 1 # front를 뒤로 한 칸 옮기고
#         deq = q[f]
#         q[f] = 0
#         return deq

def pwd(arr):
    while True:
        for i in range(1, 6):
            num = arr.pop(0) # 가장 처음 원소
            arr.append(num-i)

            if arr[-1] <= 0:
                arr[-1] = 0 # 마지막 값 setting
                return arr


T = 10
for _ in range(1, T+1):
    test_case = int(input())
    nums = list(map(int, input().split()))

    password = pwd(nums)

    print("#{}".format(test_case), end=" ")
    print(*password)


"""
다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.

- 8개의 숫자를 입력 받는다.

- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다. 

다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.

이와 같은 작업을 한 사이클이라 한다.

- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.
"""


