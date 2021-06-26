# 유기농 배추
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,0,1,0]
dy = [0,-1,0,1]
t = int(input())
while t != 0:
    m,n,k = map(int,input().split())
    board = [[0 for i in range(m)] for _ in range(n)]
    dist = [[False for i in range(m)] for _ in range(n)]
    for i in range(k):
        a,b = map(int,input().split())
        board[b][a] = 1
    cnt = 0

    for a in range(n):
        for b in range(m):
            if board[a][b] == 0:
                continue
            if dist[a][b] == True:
                continue
            cnt += 1
            q = deque()
            q.append((a,b))
            dist[a][b] = True
            while q:
                x,y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if board[nx][ny] == 0 or dist[nx][ny] == True:
                        continue
                    dist[nx][ny] = True
                    q.append((nx,ny))
    
    print(cnt)
    t -= 1

