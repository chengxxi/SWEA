# 1208: Flatten

for test_case in range(1,11):
    dump = int(input())
    boxes = list(map(int, input().split()))
     
    while dump >= 0 :
        max_height = min_height = boxes[0] # 최대 / 최소 높이
        for box in boxes:
            if box >= max_height:
                max_height = box # max height
            if box <= min_height:
                min_height = box # min height
         
        # max와 min의 위치를 찾아, 그 위치에 있는 높이를 +/- 1 처리
        max_idx = boxes.index(max_height)
        min_idx = boxes.index(min_height)
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        
        # dump의 수 차감
        dump -= 1
         
     # gap btw max / min height
    gap = max_height - min_height    
    print(f"#{test_case} {gap}")

"""
한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 
제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.
"""