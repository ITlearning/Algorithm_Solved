# 음식물 피하기
import sys
from collections import deque
n,m,k = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

board = [[0 for i in range(m)] for i in range(n)]
dist = [[0 for i in range(m)] for i in range(n)]
for _ in range(k):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1

def dfs(x,y, cnt):
    dist[x][y] = 1
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and dist[nx][ny] == 0:
                dist[nx][ny] = 1
                q.append((nx,ny))
                cnt += 1

    return cnt

z = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and dist[i][j] == 0:
            cnt = dfs(i,j, 1)
            z = max(z, cnt)
print(z)