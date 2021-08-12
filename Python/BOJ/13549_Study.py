# 숨바꼭질 3
import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

dist = [0] * (100001)
time = 0

q = deque()

q.append([n,0])
total = 0
while q:
    x, time = q.popleft()
    if x == k:
        total = time
        print(time)
        break
    
    if x*2 >= 0 and x*2 < 100001:
        if dist[x*2] == 0:
            dist[x*2] = 1
            q.append([x*2,time])
        

    for i in (x-1, x+1):
        if i >= 100001 or i < 0:
                continue
        if dist[i] == 0:
            dist[i] = 1
            q.append([i, time+1])
