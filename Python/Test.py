from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*(bridge_length)
    truck_weights = deque(truck_weights)
    bridge = deque(bridge)
    cnt = 0
    total = 0
    while len(bridge) != 0:
        num = bridge.popleft()
        total -= num
        
        cnt += 1
        
        if truck_weights:
            if total + truck_weights[0] <= weight:
                m = truck_weights.popleft()
                total += m
                bridge.append(m)
            else:
                bridge.append(0)
                   
    return cnt