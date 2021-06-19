# 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
board = [list(input().rstrip()) for _ in range(N)]
dist = [[0]*(M) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]


def dfs(x,y):
    q = deque()
    q.append((x,y))
    dist[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == '0' or dist[nx][ny] > 0:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx,ny))
 
dfs(0,0)

print(dist[N-1][M-1])