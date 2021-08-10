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
total = 0

def bfs(i,j):
    global change_box
    q = deque()
    q.append([i,j])
    change_box.append([i,j])
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue
            if dist[nx][ny] == True or board[nx][ny] != board[x][y]:
                continue
            dist[nx][ny] = True
            q.append([nx,ny])
            change_box.append([nx,ny])

def down():
    for i in range(6):
        for j in range(10,-1,-1):
            for k in range(11,j,-1):
                if board[j][i] != "." and board[k][i] == ".":
                    board[k][i] = board[j][i]
                    board[j][i] = "."


while True:
    isTrue = False
    dist = [[False for _ in range(6)] for i in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] == "." or dist[i][j]:
                continue
            dist[i][j] = True
            change_box = []
            bfs(i,j)
            if len(change_box) >= 4:
                isTrue = True
                for x,y in change_box:
                    board[x][y] = "."
    if isTrue == False:
        break
    down()
    total += 1
print(total)