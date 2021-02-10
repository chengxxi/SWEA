# 1966. 숫자를 정렬하자

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
 
    for i in range(N-1):
        for j in range(i+1, N):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
     
    print("#{} {}".format(test_case, " ".join(map(str, numbers))))


"""
주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
"""