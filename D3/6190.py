# 6190. 정곤이의 단조 증가하는 수

for test_case in range(1, int(input()) + 1):
    N = int(input())  # number of integers
    nums = list(map(int, input().split()))  # numbers

    muls = []
    # for i in nums:
    #     for j in nums:
    #         if i != j: muls.append(i * j)
    '''
    위의 코드로는 49개만 맞았는데, 아래처럼 바꿔서 숫자는 겹쳐도 idx가 다르게 했더니 성공
    EX:
    1
    4
    2 5 5 3
    처음 정답: 15 => 25로 변경
    '''

    for i in range(N):
        for j in range(N):
            if i != j:
                muls.append(nums[i] * nums[j])

    muls = sorted(set(muls))


    '''
    역순 / break 안 했더니 44개만 맞고 시간초과 뜸
    '''
    incnum = -1
    for m in muls[::-1]:
        m = str(m); cnt = 0
        for i in range(len(m)-1):
            if m[i] <= m[i+1]:
                cnt += 1
            else:
                break
        if cnt == len(m)-1:
            incnum = int(m)
            break

    print("#{} {}".format(test_case, incnum))


"""
정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.

그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.

어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.

예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.

양의 정수 N 개 A1, …, AN이 주어진다.

 1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.
"""