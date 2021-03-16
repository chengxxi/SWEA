# 4613: 러시아 국기 같은 깃발

def perm(idx, sub_sum):
    global ans

    # 유망성 검사: 아래 조건문에 걸리면 가지치기
    if sub_sum > n:
        return
    if idx == 3:
        if sub_sum == n:
            cnt = 0
            st = sel[0]
            st2 = st + sel[1]

            # white
            for i in flag[:st]: # flag의 시작 ~ st까지
                for j in i:
                    if j != 'W':
                        cnt += 1
            # blue
            for i in flag[st:st2]: # st ~ st2
                for j in i:
                    if j != 'B':
                        cnt += 1

            # red
            for i in flag[st2:]: # st2 ~
                for j in i:
                    if j != 'R':
                        cnt += 1

            if ans > cnt:
                ans = cnt # mininum value
        return

    # 중복순열 응용
    for i in range(1, n-1): # 각각 최소 한 줄 씩은 써야하므로
        sel[idx] = i
        perm(idx+1, sub_sum + i)




for test_case in range(1, int(input())+1):
    n, m = map(int, input().split()) # N X M
    flag = [list(input()) for _ in range(n)]

    sel = [0] * 3
    ans = 987654321

    perm(0, 0) # index, 중간 합


    print("#{} {}".format(test_case, ans))


"""
2016년은 삼성전자가 러시아 현지법인을 설립한지 20주년이 된 해이다. 이를 기념해서 당신은 러시아 국기를 만들기로 했다.

먼저 창고에서 오래된 깃발을 꺼내왔다. 이 깃발은 N행 M열로 나뉘어 있고, 각 칸은 흰색, 파란색, 빨간색 중 하나로 칠해져 있다.

당신은 몇 개의 칸에 있는 색을 다시 칠해서 이 깃발을 러시아 국기처럼 만들려고 한다. 다음의 조건을 만족해야 한다.

위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 한다.
다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 한다.
나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 한다.

이렇게 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값을 구하여라.
"""