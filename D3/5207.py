# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색 [D3]

def binarysearch(arr, k): # array, key
    global cnt
    low = 0
    high = len(arr) - 1
    dir = 0 # direction: low or high

    while low <= high:
        middle = (low + high) // 2

        if arr[middle] == k:
            cnt += 1
            return
        elif arr[middle] > k:
            if dir == 1:
                return
            else:
                high = middle - 1
                dir = 1
        else:
            if dir == 2:
                return
            else:
                low = middle + 1
                dir = 2
    return 0 # if not found

# def binarysearch(arr, l, h, t): # array, low, high, target
#     global cnt
#
#     while l <= h:
#         mid = (l + h) // 2
#         if arr[mid] == t:
#             cnt += 1
#             return
#         elif arr[mid] > t:
#             h = mid - 1
#         else:
#             l = mid + 1
#
#     return


    # if l > h:
    #     return 0
    # else:
    #     mid = (l + h) // 2
    #     if arr[mid] == k:
    #         cnt += 1
    #         return # 1
    #     elif arr[mid] > k:
    #         return binarysearch(arr, l, mid-1, k)
    #     else:
    #         return binarysearch(arr, mid + 1, h, k)




for test_case in range(1, int(input())+1):
    a, b = map(int, input().split())
    groupa = sorted(list(map(int, input().split())))
    groupb = list(map(int, input().split()))


    cnt = 0

    for i in groupb:
        c = binarysearch(groupa, i)
        # cnt += c


    print('#{} {}'.format(test_case, cnt))



'''
서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다. 그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.

전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면, 중심 원소의 인덱스 m=(l+r)//2 이고, 이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다.

이때 B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.

다음은 10개의 정수가 저장된 리스트 A에서 이진 탐색으로 6을 찾는 예이다.


6은 탐색 과정에서 양쪽을 번갈아 가며 선택하게 된다.


예를 들어 10을 찾는 경우 오른쪽-오른쪽 구간을 선택하므로 조건에 맞지 않는다

5를 찾는 경우 m에 위치하므로 조건에 맞는다.

이때 m에 찾는 원소가 있는 경우 방향을 따지지 않는다. M개의 정수 중 조건을 만족하는 정수의 개수를 알아내는 프로그램을 만드시오.
'''