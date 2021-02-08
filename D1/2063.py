# 2063. 중간값 찾기

N = int(input())
nums = list(map(int, input().split()))
middle = int(N/2)
nums = sorted(nums)
print(nums[middle])

"""
중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.

입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.
"""
