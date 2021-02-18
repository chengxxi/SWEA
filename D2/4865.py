# 4865: 글자수

T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    # count each characters in str1
    cnt = {}
    for s in str1:
        cnt[s] = 0
        
    # if a character in str2 is in str1: count + 1
    for char in str2:
        if char in cnt.keys():
            cnt[char] += 1

    # find the most frequent number
    most_freq = 0
    for nums in cnt.values():
        if nums > most_freq:
            most_freq = nums        


    print("#{} {}".format(test_case, most_freq))

"""
두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 
그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.

예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 
가장 많은 글자가 되고 3을 출력한다.

파이썬의 경우 딕셔너리를 이용할 수 있다.

"""