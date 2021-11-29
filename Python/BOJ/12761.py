# 돌다리 
from collections import deque
A, B, dong_gyu, jumi = map(int,input().split())

rock_bridge = [999999999] * (100001)

q = deque()
q.append(dong_gyu)

rock_bridge[dong_gyu] = 1

while q:
    x = q.popleft()
    if x == jumi:
        print(rock_bridge[x]-1)
        break

    for i in (x-1, x+1, x+A, x+B, x*A, x*B, x-A, x-B):
        if 0 < i < 100001:
            if rock_bridge[i] == 999999999:
                rock_bridge[i] = rock_bridge[x] + 1
                q.append(i)