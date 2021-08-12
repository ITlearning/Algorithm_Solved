# 토마토
import sys
from collections import deque
input = sys.stdin.readline
m,n,h = map(int,input().split()) 
board = []

dx = [0,-1,0,1,0,0]
dy = [-1,0,1,0,0,0]
dz = [0,0,0,0,-1,1]


for i in range(h) :
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,input().split())))
    board.append(tmp)
print(board)
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                q.append((i,j,k))

while q:
    z,x,y = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
            continue
        if board[nz][nx][ny] == 0:
            board[nz][nx][ny] = board[z][x][y] + 1
            q.append((nz,nx,ny))

total = 0
t = True
for z in board:
    for x in z:
        for y in x:
            if y == 0:
                t = False
            total = max(total, y)

if t:
    print(total-1)
else:
    print(-1)