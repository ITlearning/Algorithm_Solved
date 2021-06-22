# 음려수 얼려먹기
from collections import deque
N,M = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,-1,0,1]
board = []
dist = [[0]*(M) for i in range(N)]
for i in range(N):
    board.append(list(input().rstrip()))

def dfs(i,j):
    dist[i][j] = 1
    q = deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == '1' or dist[nx][ny] == 1:
                continue
            dist[nx][ny] = 1
            q.append((nx,ny))
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '1' or dist[i][j] == 1:
            continue
        dfs(i,j) 
        cnt += 1
        
print(cnt)