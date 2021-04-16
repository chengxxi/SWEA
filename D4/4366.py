# 4366. 정식이의 은행업무
'''
7/10
'''

def bin2dec(num): # 2 -> 10
    ans = 0
    for i in range(len(str(num))):
        ans += int(str(num)[i]) * 2 ** (len(str(num))-1 - i)
    return ans

def ter2dec(num): # 3 -> 10
    ans = 0
    for i in range(len(str(num))):
        ans += int(str(num)[i]) * 3 ** (len(str(num))-1 - i)
    return ans


def possibleb(b): # possible binary numbers
    global bins
    bin = list(str(b))
    for i in range(len(bin)):
        if bin[i] == '0':
            tmp = bin[::]
            tmp[i] = '1'
            bins.append(tmp)

        elif bin[i] == '1':
            tmp2 = bin[::]
            tmp2[i] = '0'
            bins.append(tmp2)

    return bins


def possiblet(t): # possible ternary numbers
    global ters
    ter = list(str(t))
    for i in range(len(ter)):
        if ter[i] == '0':
            tmp = ter[::]
            tmp[i] = '1'
            ters.append(tmp)

            tmp[i] = '2'
            ters.append(tmp)

        elif ter[i] == '1':
            tmp = ter[::]
            tmp[i] = '0'
            ters.append(tmp)

            tmp[i] = '2'
            ters.append(tmp)

        elif ter[i] == '2':
            tmp = ter[::]
            tmp[i] = '0'
            ters.append(tmp)

            tmp[i] = '1'
            ters.append(tmp)

    return ters

def list2int(li): # make integers from each list in lists
    ints = []
    for l in li:
        integer = ''
        for i in l:
            integer += i
        ints.append(integer)
    return ints

def comparing(bin, ter):
    nums = []
    for b in bin:
        b = bin2dec(int(b))
        nums.append(b)
    for t in ter:
        t = ter2dec(int(t))
        nums.append(t)

    for n in nums:
        if nums.count(n) == 2:
            return n

for test_case in range(1, int(input())+1):
    binary = int(input())
    ternary = int(input())

    # bin = bin2dec(binary)
    # ter = ter2dec(tenary)

    bins = []
    ters = []
    possibleb(binary) # possible binary numbers
    possiblet(ternary) # possible ternary # 4366. 정식이의 은행업무

def bin2dec(num): # 2 -> 10
    ans = 0
    for i in range(len(str(num))):
        ans += int(str(num)[i]) * 2 ** (len(str(num))-1 - i)
    return ans

def ter2dec(num): # 3 -> 10
    ans = 0
    for i in range(len(str(num))):
        ans += int(str(num)[i]) * 3 ** (len(str(num))-1 - i)
    return ans


def possibleb(b): # possible binary numbers
    global bins
    bin = list(str(b))
    for i in range(len(bin)):
        if bin[i] == '0':
            tmp = bin[::]
            tmp[i] = '1'
            bins.append(tmp)

        elif bin[i] == '1':
            tmp2 = bin[::]
            tmp2[i] = '0'
            bins.append(tmp2)

    return bins


def possiblet(t): # possible ternary numbers
    global ters
    ter = list(str(t))
    for i in range(len(ter)):
        if ter[i] == '0':
            tmp = ter[::]
            tmp[i] = '1'
            ters.append(tmp)

            tmp[i] = '2'
            ters.append(tmp)

        elif ter[i] == '1':
            tmp = ter[::]
            tmp[i] = '0'
            ters.append(tmp)

            tmp[i] = '2'
            ters.append(tmp)

        elif ter[i] == '2':
            tmp = ter[::]
            tmp[i] = '0'
            ters.append(tmp)

            tmp[i] = '1'
            ters.append(tmp)

    return ters

def list2int(li): # make integers from each list in lists
    ints = []
    for l in li:
        integer = ''
        for i in l:
            integer += i
        ints.append(integer)
    return ints

def comparing(bin, ter):
    nums = []
    for b in bin:
        b = bin2dec(int(b))
        nums.append(b)
    for t in ter:
        t = ter2dec(int(t))
        nums.append(t)

    for n in nums:
        if nums.count(n) >= 2:
            return n

for test_case in range(1, int(input())+1):
    binary = int(input())
    ternary = int(input())

    # bin = bin2dec(binary)
    # ter = ter2dec(tenary)

    bins = []
    ters = []
    possibleb(binary) # possible binary numbers
    possiblet(ternary) # possible ternary numbers

    lb = list(set(list2int(bins))) # set of binary integers
    lt = list(set(list2int(ters))) # set of ternary integers

    answer = comparing(lb, lt)



    print('#{} {}'.format(test_case, answer))



'''
삼성은행의 신입사원 정식이는 실수를 저질렀다.

은행 업무가 마감되기 직전인 지금, 송금할 금액을 까먹고 말았다.

하지만 다행스럽게도 정식이는 평소 금액을 2진수와 3진수의 두 가지 형태로 기억하고 다니며,
기억이 명확하지 않은 지금조차 2진수와 3진수 각각의 수에서 단 한 자리만을 잘못 기억하고 있다는 것만은 알고 있다.

예를 들어 현재 기억이 2진수 1010과 3진수 212을 말해주고 있다면 이는 14의 2진수인 1110와
14의 3진수인 112를 잘못 기억한 것이라고 추측할 수 있다.

정식이는 실수를 바로잡기 위해 당신에게 부탁을 하였다.

정식이가 송금액을 추측하는 프로그램을 만들어주자.

( 단, 2진수와 3진수의 값은 무조건 1자리씩 틀리다.  추측할 수 없는 경우는 주어지지 않는다. )
'''numbers

    lb = list(set(list2int(bins))) # set of binary integers
    lt = list(set(list2int(ters))) # set of ternary integers

    answer = comparing(lb, lt)



    print('#{} {}'.format(test_case, answer))



'''
삼성은행의 신입사원 정식이는 실수를 저질렀다.

은행 업무가 마감되기 직전인 지금, 송금할 금액을 까먹고 말았다.

하지만 다행스럽게도 정식이는 평소 금액을 2진수와 3진수의 두 가지 형태로 기억하고 다니며,
기억이 명확하지 않은 지금조차 2진수와 3진수 각각의 수에서 단 한 자리만을 잘못 기억하고 있다는 것만은 알고 있다.

예를 들어 현재 기억이 2진수 1010과 3진수 212을 말해주고 있다면 이는 14의 2진수인 1110와
14의 3진수인 112를 잘못 기억한 것이라고 추측할 수 있다.

정식이는 실수를 바로잡기 위해 당신에게 부탁을 하였다.

정식이가 송금액을 추측하는 프로그램을 만들어주자.

( 단, 2진수와 3진수의 값은 무조건 1자리씩 틀리다.  추측할 수 없는 경우는 주어지지 않는다. )
'''