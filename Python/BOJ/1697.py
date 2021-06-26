# 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline
dist = [-1] * 100001
n,k = map(int,input().split())

q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x == k:
        print(dist[x]+1)
        break
    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= 100000:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)