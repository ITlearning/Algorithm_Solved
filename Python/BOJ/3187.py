# 양치기 꿍
# 양
import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())
wolf = 0
sheep = 0
board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for a in range(r):
    board.append(list(input().rstrip()))
dist= [[0] * (c) for _ in range(r)]

total_Sheep = 0
total_Wolf = 0

def dfs(x,y) :
    global wolf, sheep
    dist[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if board[x][y] == "v":
            wolf += 1
        elif board[x][y] == "k":
            sheep += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != "#" and dist[nx][ny] == 0:
                q.append((nx, ny))
                dist[nx][ny] = 1


for i in range(r):
    for j in range(c):
        if board[i][j] != "#" and dist[i][j] == 0:
            wolf = 0
            sheep = 0
            dfs(i,j)
            if wolf >= sheep:
                sheep = 0
            else:
                wolf = 0
            total_Sheep += sheep
            total_Wolf += wolf

print(total_Sheep, total_Wolf)