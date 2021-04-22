# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산 [D4]


for test_case in range(1, int(input())+1):
    number, target = map(int, input().split())
    visited = [0] * 1000001

    queue = [(target, 0)] # 역으로 target & cnt
    while queue:
        temp = queue.pop(0)

        if temp[0] == number: # target == number
            break

        else:
            # // 2
            if temp[0] % 2 == 0 and temp[0] // 2 > 1 and not visited[temp[0]//2]:
                visited[temp[0]//2] == 1 # mark as visited
                queue.append((temp[0]//2, temp[1]+1))
            # + 10
            if temp[0] + 10 <= 1000000 and not visited[temp[0]+10]:
                visited[temp[0]+10] = 1
                queue.append((temp[0]+10, temp[1]+1))
            # + 1
            if temp[0] + 1 <= 1000000 and not visited[temp[0]+1]:
                visited[temp[0]+1] = 1
                queue.append((temp[0]+1, temp[1]+1))
            # - 1
            if temp[0] - 1 > 0 and not visited[temp[0]-1]:
                visited[temp[0]-1] = 1
                queue.append((temp[0]-1, temp[1]+1))


    cnt = temp[1]
    print('#{} {}'.format(test_case, cnt))


'''
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.

사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.

단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.

예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.
'''
