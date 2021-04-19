#  5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬 [D3]

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # tmp = left.pop(i)
                result.append(left[i])
                i += 1
            else:
                # tmp = right.pop(j)
                result.append(right[j])
                j += 1
        elif len(left) > i:
            # tmp = left.pop(0)
            result.append(left[i])
            i += 1
        elif len(right) > j:
            # tmp = right.pop(0)
            result.append(right[j])
            j += 1

    return result




def mergesort(arr):
    global cnt

    if len(arr) == 1: return arr

    middle = len(arr)//2
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])

    if left[-1] > right[-1]:
        cnt += 1

    return merge(left, right)




for test_case in range(1, int(input())+1):
    n = int(input()) # number of integers
    data = list(map(int, input().split()))
    length = len(data)
    result = []; cnt = 0

    data = mergesort(data)
    # print(data)
    print('#{} {} {}'.format(test_case, data[length//2], cnt))



'''
알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.

정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다.

N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.

병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.

정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.

알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.
'''