# 2025. N줄덧셈

num = int(input())
total = 0
for n in range(1, num+1):
    total += n
    
print(total)

"""
1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.

단, 주어질 숫자는 10000을 넘지 않는다.
"""