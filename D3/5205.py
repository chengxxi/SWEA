# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 [D3]

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def partition(arr, l, r):
    p = arr[l] # pivot value
    i = l; j = r
    while i <= j:
        if arr[i] <= p:
            i += 1
        if arr[j] >= p:
            j -= 1
        if i < j:
            swap(arr, i, j)


    swap(arr, l, j)

    return j


def quicksort(arr, l, r): # array, left, right
    if l >= r: return
    if l < r:
        pt = partition(arr, l, r)
        quicksort(arr, l, pt-1)
        quicksort(arr, pt+1, r)


for test_case in range(1, int(input())+1):
    n = int(input()) # number of integers
    data = list(map(int, input().split()))
    length = len(data) // 2

    quicksort(data, 0, len(data)-1)

    print('#{} {}'.format(test_case, data[length]))




'''
퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.
'''