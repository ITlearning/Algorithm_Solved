# 그림
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
art = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]
cnt = 0
def dfs(x,y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == 1:
            dfs(nx,ny)



for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            cnt = 0
            dfs(i,j)
            art.append(cnt)

if len(art) == 0:
    print(len(art))
    print(0)
else:
    print(len(art))
    print(max(art))