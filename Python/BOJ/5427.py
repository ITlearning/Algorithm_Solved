# 불
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
dx = [-1,0,1,0]
dy = [0,-1,0,1]
while T != 0:
    W,H = map(int,input().split())
    board = [list(input().rstrip()) for _ in range(H)]
    dist = [[-1]*(W) for _ in range(H)]
    fdist = [[-1]*(W) for _ in range(H)]
    Q1 = deque()
    Q2 = deque()

    for a in range(H):
        for b in range(W):
            if board[a][b] == '*':
                Q1.append((a,b))
                fdist[a][b] = 0
            elif board[a][b] == '@':
                Q2.append((a,b))
                dist[a][b] = 0

    # 불 DFS
    def fdfs():
        while Q1:
            x,y = Q1.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    continue
                if fdist[nx][ny] >= 0 or board[nx][ny] == '#':
                    continue
                fdist[nx][ny] = fdist[x][y] + 1
                Q1.append((nx,ny))

    # 사람 DFS
    result = 0
    def dfs():
        while Q2:
            x,y = Q2.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    return dist[x][y]+1
                if dist[nx][ny] >= 0 or board[nx][ny] == '#':
                    continue
                if fdist[nx][ny] != -1 and fdist[nx][ny] <= dist[x][y] + 1:
                    continue
                dist[nx][ny] = dist[x][y] + 1
                Q2.append((nx,ny))
        return -1
    
    fdfs()
    te = dfs()
    if te == -1:
        print("IMPOSSIBLE")
    else:
        print(te)


    T -= 1