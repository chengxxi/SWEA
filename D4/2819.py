# 2819. 격자판의 숫자 이어 붙이기

def is_safe(x,y):
    if 0 <= x < 4 and 0 <= y < 4:
        return True
    return False # default

def dfs(x, y, num):
    global nums
    if len(num) == 7:
        if num not in nums:
            nums.add(num)
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if is_safe(nx, ny):
            dfs(nx, ny, num + str(arr[nx][ny]))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


for test_case in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(4)] # 4 x 4
    nums = set() # []: 시간초과

    for i in range(4):
        for j in range(4):
            dfs(i, j, '')

    print('#{} {}'.format(test_case, len(set(nums))))



'''
4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9 사이의 숫자가 적혀 있다.

격자판의 임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서,
각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.

이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며, 0으로 시작하는 0102001과 같은 수를 만들 수도 있다.

단, 격자판을 벗어나는 이동은 가능하지 않다고 가정한다.

격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.
'''