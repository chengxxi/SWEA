# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합

'''
세로줄에서 하나씩 추출해서 가장 작은 숫자의 합 구하기
'''

def find_min_sum(i): # i는 세로줄
    global min_sum, row_sum

    # 가지치기 : 이미 값이 더 큰 경우
    if row_sum > min_sum:
        return

    if i == n: # 끝까지 다 해봤을 때
        if row_sum < min_sum:
            min_sum = row_sum # 가장 작은 값 갱신
        return

    for j in range(n):
        if visited[j] == 0:
            visited[j] = 1 # 방문 표시
            # 중간까지의 합 row_sum
            row_sum += arr[i][j] # 깂을 더하고
            find_min_sum(i+1) # 다음 칸으로 이동

            # 각각 원상복귀
            visited[j] = 0
            row_sum -= arr[i][j]



T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [0] * n
    row_sum = 0
    min_sum = 10 * n # 이것보다 커질 수 없음 (각 자리 수는 10 미만)


    find_min_sum(0)

    print("#{} {}".format(test_case, min_sum))


"""
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.

조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.


예를 들어 다음과 같이 배열이 주어진다.

[[2, 1, 2],
[5, 8, 5],
[7, 2, 2]]

이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.
"""