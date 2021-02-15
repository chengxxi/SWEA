# 1204: 최빈수 구하기

T = int(input())
for test_case in range(1, T + 1):
    t = int(input())
    nums = list(map(int, input().split()))
    scores = [0] * 101 # score range : 0 ~ 100
    for n in nums: # 숫자들의 출현 횟수 카운트
        scores[n] += 1
    idx = 0       
    for m in range(len(scores)):
        if scores[m] >= scores[idx]:
            idx = m
         
    print("#{} {}".format(t, idx))

"""
어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.

이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 
여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.

다음과 같은 수 분포가 있으면,

10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3

최빈수는 8이 된다.

최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).
"""