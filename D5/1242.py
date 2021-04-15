# 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔


hex2bin = {
    '0': [0, 0, 0, 0], '1': [0, 0, 0, 1], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0], '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0], '9': [1, 0, 0, 1],'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1],'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]
}

table = {
    (2, 1, 1): 0, (2, 2, 1): 1,
    (1, 2, 2): 2, (4, 1, 1): 3,
    (1, 3, 2): 4, (2, 3, 1): 5,
    (1, 1, 4): 6, (3, 1, 2): 7,
    (2, 1, 3): 8, (1, 1, 2): 9
}

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split()) # N X M
    data = [[] for _ in range(N)]

    # 입력을 받으면서 16진수를 2진수로 변환
    for i in range(N):
        row = input()
        for j in range(M):
            data[i].extend(hex2bin[row[j]])

    # data
    result = 0
    for i in range(N):
        j = M * 4 - 1

        while j >= 55:
            if data[i][j] and data[i - 1][j] == 0:
                pwd = []

                for _ in range(8):
                    ratio3 = 0;
                    ratio2 = 0;
                    ratio1 = 0

                    while data[i][j] == 0:
                        j -= 1

                    while data[i][j] == 1:
                        ratio3 += 1
                        j -= 1

                    while data[i][j] == 0:
                        ratio2 += 1
                        j -= 1

                    while data[i][j] == 1:
                        ratio1 += 1
                        j -= 1

                    MIN = min(ratio1, ratio2, ratio3)
                    pwd.append(table[(ratio1 // MIN, ratio2 // MIN, ratio3 // MIN)])

                pwd_sum = 0
                for pwd_idx, pwd_val in enumerate(pwd):
                    if pwd_idx % 2:
                        pwd_sum += pwd_val * 3
                    else:
                        pwd_sum += pwd_val

                if pwd_sum % 10 == 0:
                    result += sum(pwd)

            else:
                j -= 1

    print('#{} {}'.format(test_case, result))