# 2007. 패턴 마디의 길이

T = int(input())

for test_case in range(1, T + 1):
    string = input()
    for p in range(1, len(string)):
        pattern = ''
        if string[0:p] == string[p:p+p]:
            pattern = string[0:p]
            break
    print("#{} {}".format(test_case, len(pattern)))

"""
패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.
"""