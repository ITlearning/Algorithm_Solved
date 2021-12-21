# 현수막
from collections import deque

m,n = map(int,input().split())
board = []
dx = [0,-1,0,1,-1,-1,1,1]
dy = [-1,0,1,0,-1,1,-1,1]

for _ in range(m):
    board.append(list(map(int,input().split())))
cnt = 0

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            cnt += 1
            q = deque()
            q.append([i,j])
            board[i][j] = 2
            
            # bfs 시작
            while q:
                x,y = q.popleft()
                for direction in range(8):
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny] == 1:
                            q.append([nx,ny])
                            board[nx][ny] = 2

print(cnt)
            