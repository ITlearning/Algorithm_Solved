# 트럭
from collections import deque
N,W,L = map(int,input().split())

board = list(map(int,input().split()))

answer = 0
bridge = [0]*(W) # 입력받은 다리 개수만큼 0 초기화
truck_weights = deque(board)
bridge = deque(bridge)
cnt = 0
total = 0

# 다리에 아-무것도 없을 때까지 ㅇㅇ
while len(bridge) != 0:
    num = bridge.popleft()
    total -= num
    cnt += 1
    
    # 아직 옮겨야 할 트럭이 있으면
    if truck_weights:
        # 지금 올려져있는 크기와 올려놓을 트럭 더해서 작으면 
        if total + truck_weights[0] <= L:
            # 빼고
            m = truck_weights.popleft()
            # 더하고
            total += m
            # 다리에 추가
            bridge.append(m)
        else:
            # 아니면 0 추가. 이 0이 카운트가 되는것임.
            bridge.append(0)
print(cnt)