# 아기 상어 2
import sys
from collections import deque
N,M = map(int,input().split())
dx = [-1,0,1,0,1,-1,-1,1]
dy = [0,-1,0,1,-1,-1,1,1]

board = []
dist = [[0] * (M+1) for _ in range(N+1)]
for i in range(N):
    board.append(list(map(int,input().split())))

q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i,j))

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0:
                    q.append((nx,ny))
                    board[nx][ny] = board[x][y] + 1
    return
            
bfs()
s_dist = 0
for i in range(N):
    for j in range(M):
        s_dist = max(s_dist, board[i][j])
                
print(s_dist-1)