# 결혼식
from collections import deque

n = int(input())
m = int(input())

board = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    board[a].append(b)
    board[b].append(a)

distance = [99999999]*(n+1)
q = deque()

q.append(1)
distance[1] = 0

while q:
    x = q.popleft()
    for i in board[x]:
        if distance[i] > distance[x]:
            distance[i] = distance[x] + 1
            q.append(i)

answer_cnt = 0
for an in distance:
    if an > 0 and an < 3:
        answer_cnt += 1

print(answer_cnt)

