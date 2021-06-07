# 특정 거리의 도시 찾기
from collections import deque
import sys
imput = sys.stdin.readline
n,m,k,x = map(int,input().split())

board = [[] for _ in range(n+1)]


for _ in range(m):
    one,two = map(int, input().split())
    board[one].append(two)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for cur in board[now]:
        if distance[cur] == -1:
            distance[cur] = distance[now] + 1
            q.append(cur)

t = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        t = True

if not t:
    print(-1)