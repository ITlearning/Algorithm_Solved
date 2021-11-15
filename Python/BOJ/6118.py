# 숨바꼭질
from collections import deque

n,m = map(int,input().split())
INF = int(1e9)
board = [[] for _ in range(n+1)]
distance = [INF] * (n+1)


for _ in range(m):
    A_i, B_i = map(int,input().split())
    board[A_i].append(B_i)
    board[B_i].append(A_i)

distance = [0]*(n+1)

q = deque()
q.append(1)
distance[1] = 1

while q:
    x = q.popleft()
    for n in board[x]:
        if distance[n] == 0:
            distance[n] = distance[x] + 1
            q.append(n)

max_num = max(distance)

print(distance.index(max_num), max_num-1, distance.count(max_num))