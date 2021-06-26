# 불!
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,-1,0,1]
dist = [[-1]*(m) for _ in range(n)]
fdist = [[-1]*(m) for _ in range(n)]
Q1 = deque()
Q2 = deque()
board = []
for i in range(n):
    board.append(list(input().rstrip()))

for i in range(n):
    for j in range(m):
        if board[i][j] == 'F':
            Q1.append((i,j))
            fdist[i][j] = 0
        elif board[i][j] == 'J':
            Q2.append((i,j))
            dist[i][j] = 0
# 불 DFS
def fdfs():
    while Q1:
        x,y = Q1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if fdist[nx][ny] >= 0 or board[nx][ny] == '#':
                continue
            fdist[nx][ny] = fdist[x][y] + 1
            Q1.append((nx,ny))

T = True
result = 0
# 지훈이 DFS
def dfs():
    while Q2:
        x,y = Q2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                return dist[x][y] + 1
            if dist[nx][ny] >= 0 or board[nx][ny] == '#':
                continue
            if fdist[nx][ny] != -1 and fdist[nx][ny] <= dist[x][y] + 1:
                continue
            dist[nx][ny] = dist[x][y] + 1
            Q2.append((nx,ny))
    return -1
fdfs()
t = dfs()
if t == -1:
    print("IMPOSSIBLE")
else:
    print(t)
    
