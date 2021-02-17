# 1221: GNS

strnum = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"] # 0 ~ 9
for test_case in range(1, int(input()) + 1):
    tc, num = map(str, input().split()) # #nth / number of numbers
    numbers = list(map(str, input().split()))
    
    tmpnum = []
    for n in numbers:
        tmp = strnum.index(n) # 그 위치의 숫자
        tmpnum.append(tmp)
    
    # sort 대신 정렬
    for i in range(len(tmpnum)-1):
        min_idx = i
        for j in range(i+1, len(tmpnum)):
            if tmpnum[j] < tmpnum[min_idx]:
                min_idx = j
        tmpnum[i], tmpnum[min_idx] = tmpnum[min_idx], tmpnum[i]
            
    # 다시 글자로 변환
    ans = []
    for t in tmpnum: # tmpnum 안에는 0 ~ 9 숫자들
        ans.append(strnum[t]) # 그 위치의 글자
        
    print(tc)
    print(*ans)

"""
숫자 체계가 우리와 다른 어느 행성이 있다. 
아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.
"""