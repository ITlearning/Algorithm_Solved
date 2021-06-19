# 토마토
import sys
from collections import deque
input = sys.stdin.readline
M,N = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = [list(map(int,input().split()))for _ in range(N)]
cnt = 0
q = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i,j))


while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            board[nx][ny] = board[x][y] + 1
            q.append((nx,ny))


t = False
result = -2
for i in board:
    for b in i:
        if b == 0:
            t = True
        result = max(result, b)

if t:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)