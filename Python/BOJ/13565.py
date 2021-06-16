# 침투
import sys
from collections import deque
input = sys.stdin.readline
m,n = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = []
dist = [[0 for i in range(n)] for i in range(m)]

for _ in range(m):
    text = list(input().rstrip())
    board.append(list(text))

def dfs(x,y):
    
    dist[x][y] = 1
    q = deque()
    q.append((x,y))
    board[x][y] = '2'
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == '0' and dist[nx][ny] == 0 :
                dist[nx][ny] = 1
                board[nx][ny] = '2'
                q.append((nx,ny))

for i in range(n):
    if board[0][i] == '0' and dist[0][i] == 0:
        dfs(0,i)

if '2' in board[m-1]:
    print("YES")
else:
    print("NO")