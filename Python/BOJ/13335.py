# 트럭
from collections import deque
N,W,L = map(int,input().split())

board = list(map(int,input().split()))

answer = 0
bridge = [0]*(W)
truck_weights = deque(board)
bridge = deque(bridge)
cnt = 0
total = 0

while len(bridge) != 0:
    num = bridge.popleft()
    total -= num
    cnt += 1
    
    if truck_weights:
        if total + truck_weights[0] <= L:
            m = truck_weights.popleft()
            total += m
            bridge.append(m)
        else:
            bridge.append(0)
print(cnt)