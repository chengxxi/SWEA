# 1209: Sum

for test_case in range(1, 11):
    t = int(input())
    # input: arr [100X100]
    arr = []; answers = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
     
    # row   
    for i in range(100):
        ans = 0
        for j in range(100):
            ans += arr[i][j]
        answers.append(ans)

    # col
    for j in range(100):
        ans = 0
        for i in range(100):
            ans += arr[i][j]
        answers.append(ans)
    
    # upperleft -> lowerright
    for i in range(100):
        ans = 0
        for j in range(100):
            if i == j:
                ans += arr[i][j]
        answers.append(ans)
        
    # upperright -> lowerleft
    for i in range(100):
        ans = 0
        for j in range(100):
            if i + j == 99:
                ans += arr[i][j]
        answers.append(ans)
    
    # max value
    max_val = answers[0]
    for answer in answers:
        if max_val <= answer:
            max_val = answer
        
    print("#{} {}".format(t, max_val))


"""
다음 100X100의 2차원 배열이 주어질 때, 
각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
"""