# 1216: 회문2

for tc in range(1, 11):
    test_case = int(input())
    arr = [list(input()) for _ in range(100)] # 100 X 100
    
    # search1: row by row
    def row(arr):
        max_len = -1 # max length of palindrome
        for i in range(100): # row
            for j in range(100, 0, -1): # available length of palindrome
                for k in range(100-j+1): # range to search
                    cnt = 0
                    for l in range(j//2):
                        if arr[i][k+l] == arr[i][j+k-l-1]: # compare: first <-> last character, and so on...
                            cnt += 1
                        if cnt == j//2: # is palindrome
                            if j > max_len:
                                max_len = j # max length of palindromes
        return max_len
    
    # search2: column by column
    def col(arr):
        max_len = -1 # max length of palindrome
        for j in range(100): # column
            for i in range(100, 0, -1): # available length of palindrome
                for k in range(100-i+1): # range to search
                    cnt = 0
                    for l in range(i//2):
                        if arr[k+l][j] == arr[i+k-l-1][j]: # compare: first <-> last character, and so on...
                            cnt += 1
                        if cnt == i//2: # is palindrome
                            if i > max_len:
                                max_len = i # max length of palindromes
        return max_len     
    
    
    lr = row(arr)
    lc = col(arr)

    result = lr if lr > lc else lc

    print("#{} {}".format(test_case, result))



"""
"기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.
"""
