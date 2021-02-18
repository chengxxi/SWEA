# 1215: 회문1

T = 11
for test_case in range(1, T+1):
    plen = int(input()) # length of palindrome
    p = 0
    arr = [list(input()) for _ in range(8)]

    def row(arr, plen, p):
        for i in range(8):
            for j in range(8-plen+1):
                for k in range(plen//2):
                    if k != plen//2 - 1:
                        if arr[i][j+k] != arr[i][j+plen-1-k]:
                            break
                    else:
                        if arr[i][j+k] == arr[i][j+plen-1-k]:
                            p += 1
        return p

    def col(arr, plen, p):
        p = 0
        for j in range(8):
            for i in range(8-plen+1):
                for k in range(plen//2):
                    if k != plen//2 - 1:
                        if arr[i+k][j] != arr[i+plen-1-k][j]:
                            break
                    else:
                        if arr[i+k][j] == arr[i+plen-1-k][j]:
                            p += 1
        return p




    if plen == 1:
        p = 128
    else:
        pr = row(arr, plen, p)
        pc = col(arr, plen, p)
        palindromes = pr + pc

    print("#{} {}".format(test_case, palindromes))


    # # row
    # pal = 0
    # for i in range(N):
    #     answer = ''
    #     for j in range(N-plen+1):
    #         for k in range(plen//2):
                
    #             if arr[i][j+k] == arr[i][j+plen-1-k]:
    #                 pal += 1
    #         if pal == plen//2: # is palindrome
    #             for l in range(j, j+plen):
    #                 answer += arr[i][l]
    #         pal = 0
    #         if answer != '':
    #             pals.append(answer)
    #     p += 1


    # # col
    # pal = 0
    # for j in range(N):
    #     answer = ''
    #     for i in range(N-plen+1):
    #         for k in range(plen//2):
    #             if arr[i+k][j] == arr[i+plen-1-k][j]:
    #                 pal += 1
    #         if pal == plen//2: # is palindrome
    #             for l in range(i, i+plen):
    #                 answer += arr[l][j]
    #         pal = 0
    #         if answer != '':
    #             pals.append(answer)

    #     p += 1


        
    #result = len(pals)

    # print("#{} {} {}".format(test_case, p, result))
    #print(*pals)
            
            
            

"""
"기러기" 또는 "level" 과 같이 거꾸로 읽어도 앞에서부터 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

주어진 8x8 평면 글자판에서 가로, 세로를 모두 보아 제시된 길이를 가진 회문의 총 개수를 구하는 문제이다.

위와 같은 글자판이 주어졌을 때, 길이가 5인 회문은 붉은색 테두리로 표시된 4개가 있으며 따라서 4를 반환하면 된다.
"""
