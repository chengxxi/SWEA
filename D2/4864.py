# 4864. 문자열 비교

T = int(input())
for test_case in range(1, T+1):
    str1 = input() # pattern to be found
    str2 = input() # total text
    len1 = len(str1) # length of pattern
    len2 = len(str2) # length of the whole text
    
    # if str1 in str2:
    #     result = 1
    # else:
    #     result = 0

    # print("#{} {}".format(test_case, result))

    ### BRUTE FORCE ###
    def BruteForce(str1, str2):
        i = 0 # index of str2
        j = 0 # index of str1
        
        while j < len1 and i < len2:
            if str2[i] != str1[j]:
                i = i - j # backstep
                j = -1
            i = i + 1
            j = j + 1 # 0
        if j == len1: # Success
            return 1 # i - len1
        else: # Fail
            return 0


    result = BruteForce(str1, str2)
    print("#{} {}".format(test_case, result))
    


"""
두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
 

ABC

ZZZZZABCZZZZZ

두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
 

ABC

ZZZZAZBCZZZZZ

문자열이 일치하지 않으므로 0을 출력.

"""