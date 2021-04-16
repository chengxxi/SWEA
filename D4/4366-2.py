# 4366. 정식이의 은행업무

# def bin2dec(num): # 2 -> 10
# #     ans = 0
#     for i in range(len(str(num))):
#         ans += int(str(num)[i]) * 2 ** (len(str(num))-1 - i)
#     return ans
#
# def ter2dec(num): # 3 -> 10
#     ans = 0
#     for i in range(len(str(num))):
#         ans += int(str(num)[i]) * 3 ** (len(str(num))-1 - i)
#     return ans


def f(b, t):
    bint = int(b, 2)
    bint = 0
    for x in b:
        bint = bint * 2 + int(x)
    bins = []
    for i in range(len(b)):
        bins.append(bint ^ (1<<i)) # 2진수의 1비트씩을 바꿔서 저장

    for i in range(len(t)):  # 3진수에서 다른 두 수로 바꿔볼 자리
        num1 = 0
        num2 = 0
        for j in range(len(t)):
            if i != j:
                num1 = num1 * 3 + int(t[j])
                num2 = num2 * 3 + int(t[j])
            else:
                num1 = num1 * 3 + (int(t[j]) + 1) % 3  # 0 -> 1, 1 -> 2, 2 -> 0
                num2 = num2 * 3 + (int(t[j]) + 2) % 3  # 0 -> 2, 1 -> 0, 2 -> 1

        if num1 in bins:
            return num1
        if num2 in bins:
            return num2


for test_case in range(1, int(input())+1):
    binary = input()
    ternary = input()

    answer = f(binary, ternary)


    print('#{} {}'.format(test_case, answer))
    # for i in range(len(t)) # 3진수에서 다른 두 수로 바꿔볼 자리
    #     num1 = 0
    #     num2 = 0
    #     for j in range(len(t)):
    #         if i != j:
    #             num1 = num1 * 3 + int(t[j])
    #             num2 = num2 * 3 + int(t[j])
    #         else:
    #             num1 = num1 * 3 + (int(t[j]) + 1) % 3 # 0 -> 1, 1 -> 2, 2 -> 0
    #             num2 = num2 * 3 + (int(t[j]) + 2) % 3 # 0 -> 2, 1 -> 0, 2 -> 1
    #
    #     if num1 in bins:
    #         return num1
    #     if num2 in bins:
    #         return num2
