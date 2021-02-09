# 4834: 숫자 카드

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = int(input())
    cnt = [0] * 10 # 0부터 9까지 각자 칸 생성

    for i in range(N): 
    # nums에 대해서 각 숫자가 얼마나 쓰였는지 count
        cnt[nums%10] += 1
        nums //= 10
        
    max_c = 0; thenum = 0; c = 0; 
    max_count = 0

    # 가장 큰 cnt 찾고, 여러개인지도 확인
    while c < 10:
        if cnt[c] >= max_c:
            thenum = c
            max_c = cnt[c]
        c += 1
            
    print(f"#{test_case} {thenum} {max_c}")

    


"""
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
"""