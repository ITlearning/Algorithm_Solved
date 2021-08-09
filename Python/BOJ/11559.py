# Puyo Puyo
from collections import deque
import sys
input = sys.stdin.readline
board = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for i in range(12):
    tmp = input().rstrip()
    board.append(list(tmp))
dist = [[False for i in range(6)] for i in range(12)]
total = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '.':# or dist[i][j]:
            continue
        
        dist[i][j] = True
        q = deque()
        q.append([i,j])
        box = deque()
        box.append([i,j])
        cnt = 1
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                    continue
                if dist[nx][ny] == True or board[nx][ny] != board[x][y]:
                    continue
                dist[nx][ny] = True
                q.append([nx,ny])
                box.append([nx,ny])
                cnt += 1
            print(cnt)
        if cnt >= 4:
            while box:
                x,y = box.popleft()
                board[x][y] == "."
            total += 1
        for i in board:
            print(i)        
print(total)
