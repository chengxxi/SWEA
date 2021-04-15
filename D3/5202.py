# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

for test_case in range(1, int(input())+1):
    N = int(input()) # number of reservation forms
    res = [list(map(int, input().split())) for _ in range(N)] # N reservations
    # sort reservations: earlier end time first
    res = sorted(res, key = lambda time: (time[1], time[0]))

    cnt = 0 # number of total reservations accepted
    last = 0 # last end time

    for time in res:
        if time[0] >= last: # start time >= last end time
            last = time[1]
            cnt += 1

    print('#{} {}'.format(test_case, cnt))



'''
24시간 운영되는 물류센터에는 화물을 싣고 내리는 도크가 설치되어 있다.

0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.

신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고,
앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.

예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다.
'''