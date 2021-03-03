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





