# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2 [D3]

def min_charge(idx, ch): # dfs: index & charging
    global charging

    if idx >= stop-1:
        if charging > ch:
            charging = ch
        return

    # prunning
    if ch >= charging:
        return

    for i in range(1, elec[idx]+1):
        min_charge(idx+i, ch+1)


for test_case in range(1, int(input())+1):
    rawdata = list(map(int, input().split()))

    stop = rawdata[0] # number of stops
    elec = rawdata[1:] # total charging centres

    charging = stop-1 # charge at every stops

    min_charge(0, 0)


    print('#{} {}'.format(test_case, charging-1))





'''
충전지를 교환하는 방식의 전기버스를 운행하려고 한다. 정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.

충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.

정류장과 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오. 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.

다음은 1번에서 출발 5번이 종점인 경우의 예이다.


정류장 1 2 3 4 5
충전지 2 3 1 1


1번에서 장착한 충전지 용량이 2이므로, 3번 정류장까지 운행할 수 있다. 그러나 2번에서 미리 교체하면 종점까지 갈 수 있다.

마지막 정류장에는 배터리가 없다.
'''