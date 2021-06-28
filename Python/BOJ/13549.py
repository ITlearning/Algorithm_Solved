# 숨바꼭질 3
import sys
from collections import deque
input = sys.stdin.readline

MAX_INDEX = 100000
dist = [-1] * (MAX_INDEX+1)

N,K = map(int,input().split())

q = deque()
q.append(N)
dist[N] = 0
while q:
    x = q.popleft()
    if x == K:
        break
    if x*2 <= MAX_INDEX and dist[x*2] == -1:
        dist[x*2] = dist[x]
        q.append(x*2)
    
    for nx in (x-1, x+1):
        if 0 <= nx <= MAX_INDEX and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)

print(dist[K])