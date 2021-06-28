# 상범 빌딩
import sys
from collections import deque
input = sys.stdin.readline

dh = [0,0,0,0,-1,1]
dx = [-1,0,1,0,0,0]
dy = [0,-1,0,1,0,0]

def dfs(h,x,y):
    q = deque()
    q.append([h,x,y])
    dist[h][x][y] = 1
    while q:
        h,x,y = q.popleft()
        for i in range(6):
            nh = h + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nh < 0 or nx >= N or ny >= M or nh >= H:
                continue
            if board[nh][nx][ny] == '#' or dist[nh][nx][ny] >= 1:
                continue
            if board[nh][nx][ny] == 'S':
                return "Escaped in " + str(dist[h][x][y]) + " minute(s)."
            dist[nh][nx][ny] = dist[h][x][y] + 1
            q.append([nh,nx,ny])
    return "Trapped!"
            

while True:
    H,N,M = map(int,input().split())
    if H == 0:
        break
    dist = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
    board = [[]*N for i in range(H)]
    for i in range(H):
        for j in range(N):
            board[i].append(list(map(str,input().rstrip())))
        input()
    for i in range(H):
        for a in range(N):
            for b in range(M):
                if board[i][a][b] == 'E':
                    print(dfs(i,a,b))
