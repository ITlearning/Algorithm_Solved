# 토마토
from collections import deque
import sys
input = sys.stdin.readline
m,n = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,-1,0,1]
q = deque()
board = []
for i in range(n):
    board.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i,j))

cnt = 0
def dfs():
    if q:
        x,y = q.popleft()
        q.append((x,y))
    while q:
        (x,y)= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                q.append((nx,ny))

dfs()
t = False
answer = -2
for i in board:
    for j in i:
        if j == 0:
            t = True
        
        answer = max(answer,j)

if t:
    print(-1)
else:
    print(answer-1)