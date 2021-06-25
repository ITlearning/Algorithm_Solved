# 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
board = []
dist = [[0]*(m) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for i in range(n):
    text = list(input().rstrip())
    board.append(list(text))
cnt = 0
def dfs(x,y):
    q = deque()
    q.append((x,y))
    dist[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == '0' or dist[nx][ny] > 1:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx,ny))

dfs(0,0)
print(dist[n-1][m-1])