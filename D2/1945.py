# 1945. 간단한 소인수분해

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    prime = [2, 3, 5, 7, 11]
    cnt = [0] * 5
    
    for i in range(len(prime)):
        while N % prime[i] == 0:
            cnt[i] += 1
            N //= prime[i]

    print("#{} {}".format(test_case, " ".join(map(str, cnt))))

"""
숫자 N은 아래와 같다.

N=2^a x 3^b x 5^c x 7^d x 11^e

N이 주어질 때 a, b, c, d, e 를 출력하라.
"""