# 수업 코드 참고

# 완전탐색을 위한 함수
def backtrack(now):
    case = ''.join(cards)
    if case in visited[now]:
        # 있으면 진행하지 않는다
        return
    # 없는 경우에 케이스 추가하고 진행
    visited[now].add(case)

    if now == count:
        global result
        result = max(result, int(case))

    else:
        for i in range(length - 1):
            for j in range(i+1, length):
                # 위에서 방문체크 이미 해서 여기서는 X

                # 다음 케이스를 위해 자리 변경
                cards[i], cards[j] = cards[j], cards[i]
                # 재귀 호출 (현재까지 바꾼 횟수 + 1)
                backtrack(now + 1)
                # 원상 복구
                cards[i], cards[j] = cards[j], cards[i]


for test_case in range(1, int(input())+1):
    data = input().split()

    cards = list(data[0])
    count = int(data[1])

    length = len(cards)
    visited = [set() for _ in range(count+1)]

    result = 0
    backtrack(0)


    print('#{} {}'.format(test_case, result))